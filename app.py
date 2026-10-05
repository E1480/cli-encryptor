from os import path
from pathlib import Path

import typer

import _lily

app = typer.Typer()

@app.command()
def encrypt(
    target: str,
    password: str,
    file: bool = typer.Option(False, "--file", "-f", help="Add file"),
    preserve_file_name: bool = typer.Option(False, "--preserve", "-p", help="Preserve the file name inside the encrypted file."),
    output_file_name: str = typer.Option("file.enc", "--out_name", "-o", help="Change the name of the outptted file")
):
    if file:
        _lily.encrypt_file(
            password,
            Path(path.abspath(target)),
            preserve_file_name,
            output_file_name
        )
    else:
        _lily.encrypt_text(password, target)


@app.command()
def decrypt(
    target: str,
    password: str,
    file: bool = typer.Option(False, "--file", "-f", help="Add file."),
    rename: str = typer.Option("", "--rename", "-r", help="Rename the output file")
):
    if file:
        _lily.decrypt_file(password, Path(path.abspath(target)), rename)
    else:
        _lily.decrypt_text(password, target)

if __name__ == "__main__":
    app()
