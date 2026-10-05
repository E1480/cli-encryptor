from pathlib import Path

from . import decrypt, encrypt


def encrypt_text(password: str, target: str):
    encrypt.text(password, target)

def encrypt_file(password: str, target: Path, preserve_file_name: bool, out_name: str):
    encrypt.file(password, target, preserve_file_name, out_name)

def decrypt_text(password: str, target: str):
    decrypt.text(password, target)

def decrypt_file(password: str, target: Path, new_file_name: str):
    decrypt.file(password, target, new_file_name)
