# type: ignore[attr-defined]
import typer
import os
import re
import boto3
from rich.console import Console
from pathlib import Path
from awstk.dashboard import DashboardFactory

app = typer.Typer()
console = Console()
dirprefix = Path.home() / '.awstk' / 'cloudwatch'
ec2 = boto3.resource('ec2', endpoint_url=os.environ.get("AWSTK_AWS_ENDPOINT_URL", None))
cw_client = boto3.client('cloudwatch', endpoint_url=os.environ.get("AWSTK_AWS_ENDPOINT_URL", None))
logs_client = boto3.client('logs', endpoint_url=os.environ.get("AWSTK_AWS_ENDPOINT_URL", None))


@app.command(name="list-ec2")
def list_ec2(tag_key: str = typer.Argument(...),
             tag_value_regex: str = typer.Argument(...),
             ec2_status: str = typer.Argument('running'),
             print_stdout: bool = typer.Option(True)):

    try:
        instances = [i for i in ec2.instances.all() if i.tags is not None and any(
            [x for x in i.tags if tag_key == x['Key'] and re.search(tag_value_regex, x['Value']) and i.state['Name'] == ec2_status])]
    except re.error:
        return

    if print_stdout:
        for instance in instances:
            keyValue = [x['Value']
                        for x in instance.tags if x['Key'] == tag_key][0]
            console.print(f"{keyValue},{instance.id}")

    return instances


@ app.command(name="generate-dashboard")
def generate_dashboard(
    tag_key: str = typer.Argument(...),
    tag_value_regex: str = typer.Argument(...),
    cpu: bool = typer.Option(False),
    mem: bool = typer.Option(False),
    disk: bool = typer.Option(False),
    log: bool = typer.Option(False),
    widget_height: int = typer.Option(6),
    widget_width: int = typer.Option(24),
    time_range: str = typer.Option('-P3H')


):
    instances = list_ec2(tag_key, tag_value_regex,
                         print_stdout=False, ec2_status='running')

    if not instances:
        console.print(f"[bold {'yellow'}]{'No EC2 instances were found.'}[/]")
        return

    if cpu:
        dashboard = DashboardFactory(time_range=time_range)
        console.print(
            f"[bold {'yellow'}]{'Generating CPUUsage Dashboard..'}[/]")
        for i, instance in enumerate(instances):
            label = [x for x in instance.tags if x['Key']
                     == tag_key][0]['Value']
            dashboard.add_cpu_widget(
                x=0, y=widget_height*i,
                instance_id=instance.id, label=label, width=widget_width, height=widget_height)

        dashboard_body = dashboard.get_dashboard_body()
        cw_client.put_dashboard(DashboardName='CPUUsage',
                                DashboardBody=dashboard_body)
        console.print(f"[bold {'yellow'}]{'CPUUsage Dashboard generated.'}[/]")

    if mem:
        dashboard = DashboardFactory(time_range=time_range)
        console.print(
            f"[bold {'yellow'}]{'Generating MemUsage Dashboard..'}[/]")
        for i, instance in enumerate(instances):
            label = [x for x in instance.tags if x['Key']
                     == tag_key][0]['Value']
            dashboard.add_mem_widget(
                x=0, y=widget_height*i,
                instance_id=instance.id, label=label, width=widget_width, height=widget_height, cw_namespace='CWAgent')

        dashboard_body = dashboard.get_dashboard_body()
        cw_client.put_dashboard(DashboardName='MemUsage',
                                DashboardBody=dashboard_body)
        console.print(f"[bold {'yellow'}]{'MemUsage Dashboard generated.'}[/]")

    if disk:
        dashboard = DashboardFactory(time_range=time_range)
        console.print(
            f"[bold {'yellow'}]{'Generating DiskUsage Dashboard..'}[/]")
        for i, instance in enumerate(instances):
            label = [x for x in instance.tags if x['Key']
                     == tag_key][0]['Value']
            dashboard.add_disk_space_widget(
                x=0, y=widget_height*i,
                instance_id=instance.id, label=label, width=widget_width, height=widget_height, cw_namespace='CWAgent')

        dashboard_body = dashboard.get_dashboard_body()
        cw_client.put_dashboard(DashboardName='DiskUsage',
                                DashboardBody=dashboard_body)
        console.print(
            f"[bold {'yellow'}]{'DiskUsage Dashboard generated.'}[/]")


if __name__ == "__main__":
    app()
