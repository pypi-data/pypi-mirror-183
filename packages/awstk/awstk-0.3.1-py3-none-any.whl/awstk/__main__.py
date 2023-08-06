# type: ignore[attr-defined]
import typer
from rich.console import Console

import awstk.cloudformation as cloudformation
import awstk.secretsmanager as secretsmanager
import awstk.cloudwatch as cloudwatch
import awstk.closest_match as closest_match


app = typer.Typer(name="awstk", add_completion=True)
app.add_typer(cloudformation.app, name="cloudformation")
app.add_typer(secretsmanager.app, name="secretsmanager")
app.add_typer(cloudwatch.app, name="cloudwatch")
app.add_typer(closest_match.app, name="closest-match")
console = Console()

if __name__ == "__main__":
    app()
