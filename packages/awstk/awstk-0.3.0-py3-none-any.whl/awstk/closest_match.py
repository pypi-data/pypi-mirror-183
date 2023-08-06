# type: ignore[attr-defined]
import typer
import mimetypes
import difflib
import os
from pathlib import Path
from typing import List
from rich.console import Console

app = typer.Typer()
font_color = 'green'
console = Console()


@app.command()
def find(target_file: Path, target_directories: List[Path]):
    console.print(
        f"[{font_color}]Finding closest matching file {target_file}... [/]")
    if not Path.exists(target_file):
        console.print(f"[{font_color}]{target_file} does not exist. [/]")
        return
    if any([not os.path.isdir(target_directory) for target_directory in target_directories]):
        console.print(
            f"[{font_color}]One or more of directories does not exist. [/]")
        return

    dirs = []
    for target_directory in target_directories:
        dirs += [path for path in target_directory.glob(
            f"**") if not any(part.startswith('.') for part in path.parts)]

    fpaths = []
    for d in dirs:
        files = os.listdir(d)
        fpaths += [os.path.join(d, f)
                   for f in files if os.path.isfile(os.path.join(d, f)) and not f.startswith('.')]
    f_txt = [f for f in fpaths if mimetypes.guess_type(
        f)[0] == None or 'text' in mimetypes.guess_type(f)[0]]

    f_txt_with_wc = []
    for txt in f_txt:
        console.print(f"[{font_color}]Checking {txt}..[/]")
        target_file_contents = open(
            target_file, 'r').read().splitlines(keepends=True)
        cmp_file_contents = open(txt, 'r').read().splitlines(keepends=True)
        raw_diff = list(difflib.ndiff(target_file_contents, cmp_file_contents))
        diff = [d for d in raw_diff if d.startswith('+') or d.startswith('-')]
        wc = len(diff)
        f_txt_with_wc += [(txt, wc)]

    results = sorted(f_txt_with_wc, key=lambda tup: tup[1])
    for result in results:
        console.print(f"[{font_color}]{result[0]}:{result[1]}[/]")


if __name__ == "__main__":
    app()
