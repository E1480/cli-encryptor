from pathlib import Path

from ._generate_header import Header
from ._generate_key import generate_key


def text(password: str, target: str):
    salt, fern = generate_key(password)
    enc = fern.encrypt(bytes(target.encode())).decode()
    print(f"{salt.hex()}{enc}")


def file(password: str, target: Path, preserve_file_name: bool, out_name: str):
    salt, fern = generate_key(password)
    data = None
    suffix = target.suffix[1:].encode()
    name = target.stem.encode()
    header: bytes

    with open(target, 'rb') as file:
        data = file.read()

    if preserve_file_name:
        header = Header(
            preserve_file_name,
            len(suffix),
            len(name)
        ).pack()

        write_blob = bytes(
            salt + fern.encrypt(name + suffix + data)
        )

    else:
        if not suffix and name.startswith(b"."):
                suffix = name[1:]
        header = Header(
            False,
            len(suffix),
        ).pack()

        write_blob = bytes(
            salt + fern.encrypt(suffix + data)
        )

    with open(out_name, 'wb') as file:

        for b in header:
            _ = file.write(b.to_bytes(byteorder="little"))
        _ = file.write(write_blob)
