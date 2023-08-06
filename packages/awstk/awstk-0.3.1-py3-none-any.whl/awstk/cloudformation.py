# type: ignore[attr-defined]
import typer
import subprocess
import time
import ast
import re
import os
from typing import Optional
import json
from collections import OrderedDict
from rich.console import Console
from typing import List
import boto3
import awstk.db as db
from pathlib import Path
import shutil
from botocore.exceptions import ClientError

app = typer.Typer()
font_color = 'red'
console = Console()
cfn = boto3.resource('cloudformation', endpoint_url=os.environ.get("AWSTK_AWS_ENDPOINT_URL", None))
_db = db.get_connection(tablename='cloudformation')
dirprefix = Path.home() / '.awstk' / 'cloudformation'
valid_status = ['CREATE_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_COMPLETE', 'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_COMPLETE',
                'UPDATE_ROLLBACK_FAILED', 'UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS', 'UPDATE_ROLLBACK_COMPLETE', 'REVIEW_IN_PROGRESS']


@app.command()
def mirror(target_stack_regex_list: List[str]):
    console.print(
        f"[{font_color}]{'Cloudformation: Mirroring non-updating stacks into local database..'}[/]")

    all_stacks = [stack for stack in cfn.stacks.all(
    ) if stack.stack_status in valid_status]

    stacks = []
    if target_stack_regex_list:
        for stack in all_stacks:
            is_valid_stack = any([re.search(target_stack_regex, stack.name)
                                 for target_stack_regex in target_stack_regex_list])
            if is_valid_stack:
                stacks.append(stack)

    if not stacks:
        console.print(
            f"[{font_color}]{'No stacks found. Exiting..'}[/]")
        return

    for s in stacks:
        j = cfn.meta.client.get_template(StackName=s.name)['TemplateBody']
        if type(j) == str:
            j = str(j)
        elif type(j) == OrderedDict:
            j = str(json.dumps(j))
        else:
            raise ValueError

        console.print(f"[{font_color}]{s.name}[/] done.")
        _db[s.name] = {'templatebody': j,
                       'parameters': json.dumps(s.parameters)}
        _db.commit()
        time.sleep(1)

@app.command()
def list(local: bool = False):
    if local:
        all_stacks = _db.keys()
    else:
        all_stacks = [stack.name for stack in cfn.stacks.all() if stack.stack_status in valid_status]

    for stackname in all_stacks:
        console.print(stackname)
        

@ app.command()
def edit(target_stack_name: str, edit_immediately: bool = True):
    dirpath = dirprefix / target_stack_name

    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
    os.makedirs(dirpath)
    f_parameters = open(dirpath / 'parameters.yaml', "w")
    f_templatebody = open(dirpath / 'template.yaml', "w")

    try:
        blob = _db[target_stack_name]

        f_parameters.write(blob['parameters'])
        f_templatebody.write(blob['templatebody'])

    except KeyError:
        console.print(f"[{font_color}] Stack Not Found. Available stacks: [/]")
        for key in _db.keys():
            console.print(key)
        console.print(f"[{font_color}] Creating template stack files.. [/]")
        f_parameters.write(
            '[{"ParameterKey": "SampleParameter", "ParameterValue": "SampleValue"}]')
        f_templatebody.write('Resources:')

    f_parameters.close()
    f_templatebody.close()
    console.print(f"[{font_color}]Stack ready to edit at {dirpath}[/]")

    if edit_immediately:
        subprocess.run([os.environ.get("EDITOR", "vim"), dirpath])


@ app.command()
def save(target_stack_name: str):
    try:
        dirpath = dirprefix / target_stack_name

        f_parameters = open(dirpath / 'parameters.yaml', "r").read()
        f_templatebody = open(dirpath / 'template.yaml', "r").read()

        cfn.meta.client.validate_template(TemplateBody=f_templatebody)

        _db[target_stack_name] = {'templatebody': f_templatebody,
                                  'parameters': f_parameters}

        _db.commit()
        console.print(f"[{font_color}]Stack successfully saved.[/]")

    except FileNotFoundError:
        console.print(f"[{font_color}] Stack files not found in {dirpath}.[/]")


@ app.command()
def update(target_stack_name: str, use_change_set: bool = True):
    try:
        tb = _db[target_stack_name]['templatebody']
        p = _db[target_stack_name]['parameters']
        C = ['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND']
        if p == 'null':
            p = '[]'

        if use_change_set:
            cfn.meta.client.create_change_set(
                StackName=target_stack_name, TemplateBody=tb, Parameters=ast.literal_eval(p), Capabilities=C, ChangeSetName=target_stack_name)
            console.print(
                f"[{font_color}]Changeset created. Check AWS Cloudformation UI for review.[/]")
        else:
            cfn.meta.client.update_stack(
                StackName=target_stack_name, TemplateBody=tb, Parameters=ast.literal_eval(p), Capabilities=C)
            console.print(
                f"[{font_color}]Stack update initiated. Check AWS Cloudformation UI for any updates.[/]")
    except KeyError:
        console.print(f"[{font_color}] Stack Not Found. Available stacks: [/]")
        for key in _db.keys():
            console.print(key)
        return
    except ClientError as e:
        if "does not exist" in str(e):
            cfn.meta.client.create_stack(
                StackName=target_stack_name, TemplateBody=tb, Parameters=ast.literal_eval(p), Capabilities=C)
            console.print(
                f"[{font_color}]Stack didn't exist and is being created. Check AWS Cloudformation UI for any updates.[/]")
        else:
            raise e


if __name__ == "__main__":
    app()
