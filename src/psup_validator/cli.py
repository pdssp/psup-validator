from pathlib import Path
from typing import Annotated

import typer

import psup_validator.funcs as F

app = typer.Typer(help="Validator for PSUP")

CatalogArg = typer.Argument(
    exists=True,
    file_okay=True,
    dir_okay=True,
    writable=False,
    readable=True,
    resolve_path=True,
)


@app.callback()
def callback():
    """
    PSUP-Validator
    """


@app.command()
def validate_catalog(output_path: Annotated[Path, CatalogArg]):
    """
    Validates catalog provided with the source file
    """
    F.validate_catalog(output_path)
