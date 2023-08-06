# type: ignore[attr-defined]
import typer
import subprocess
import json
import os
import shutil
from pathlib import Path
from rich.console import Console
import boto3
from botocore.exceptions import ClientError

app = typer.Typer()
font_color = 'blue'
console = Console()
smgr_client = boto3.client('secretsmanager', endpoint_url=os.environ.get("AWSTK_AWS_ENDPOINT_URL", None))
dirprefix = Path.home() / '.awstk' / 'secretsmanager'


@app.command()
def edit(target_secret_name: str, edit_immediately: bool = True):
    sanitized_secret_name = target_secret_name.replace('/', '.')
    dirpath = dirprefix / sanitized_secret_name

    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
    os.makedirs(dirpath)
    f_secret_string = open(dirpath / 'secret_string.yaml', "w")

    try:
        secret = json.loads(smgr_client.get_secret_value(
            SecretId=target_secret_name)['SecretString'])
        json.dump(secret, f_secret_string, indent=4)
    except smgr_client.exceptions.ResourceNotFoundException:
        console.print(
            f"[{font_color}]Secret doesn't currently exist. Creating template file.[/]")
        json.dump({'key': 'value'}, f_secret_string, indent=4)

    f_secret_string.close()

    console.print(f"[{font_color}]Secret ready to edit at {dirpath}[/]")

    if edit_immediately:
        subprocess.run([os.environ.get("EDITOR", "vim"), dirpath])


@app.command()
def update(target_secret_name: str):
    try:
        sanitized_secret_name = target_secret_name.replace('/', '.')
        dirpath = dirprefix / sanitized_secret_name

        f_secret_string = open(dirpath / 'secret_string.yaml', "r").read()

        smgr_client.update_secret(SecretId=target_secret_name,
                                  SecretString=f_secret_string)
        console.print(f"[{font_color}]Secret successfully updated.[/]")

    except FileNotFoundError:
        console.print(f"[{font_color}] Secret not found in {dirpath}.[/]")
        return

    except json.JSONDecodeError as err:
        console.print(f"Malformed secret at {dirpath}")
        start, stop = max(0, err.pos - 20), err.pos + 20
        snippet = err.doc[start:stop]
        console.print('... ' if start else '', snippet,
                      ' ...' if stop < len(err.doc) else '', sep="")
        console.print('^'.rjust(21 if not start else 25))
        return

    except ClientError as e:
        if "can't find the specified secret" in str(e):
            smgr_client.create_secret(Name=target_secret_name,
                                      SecretString=f_secret_string)
            console.print(
                f"[{font_color}]Secret didn't exist before, successfully created.[/]")
        else:
            raise e

    shutil.rmtree(dirpath)
    console.print(f"[{font_color}]Secret removed from {dirpath}.[/]")


if __name__ == "__main__":
    app()
