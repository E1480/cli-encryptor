from pathlib import Path

from ._generate_key import generate_key


def text(password: str, target: str):

    salt = bytes.fromhex(target[:32])
    _, fern = generate_key(password, salt)
    out = fern.decrypt(target[32::].encode())
    print(out.decode())


def file(password: str, target: Path, new_file_name: str):

    with open(target, 'rb') as file:
        data = file.read()

    identifier = data[0:7].decode()

    if identifier == "♥LILY":

        flag = bool(bytes(data[8] >> 7))
        #TODO: Check this ones in a while.
        version = data[8] & 0b0111_1111  # pyright: ignore[reportUnusedVariable]  # noqa: F841

        # ================ Uncomment when we have different versions =========================
        # if version == 0:
        #     decrypt, full_file_name, ext_len = _file_decrypt_0(flag, data, password)

        decrypt, full_file_name, ext_len = _file_decrypt_0(flag, data, password)

        full_file_name = full_file_name if new_file_name == "" else new_file_name

        with open(full_file_name, "w") as file:
            _ = file.write(decrypt.decode()[ext_len::].replace("\r", ""))

    else:
        raise ValueError("File not known.")


def _file_decrypt_0(flag: bool, data: bytes, password: str):
    ext_len = int.from_bytes(data[10:11], "big")
    name_len = int.from_bytes(data[12:13], "big")

    salt = data[14:30]
    data = data[30::]

    _, fern = generate_key(password, salt)
    decrypt = fern.decrypt(data)
    extenstion = decrypt[name_len:ext_len + name_len].decode()
    if flag:
        file_name = decrypt[0:name_len].decode()
        full_file_name = f"{file_name}.{extenstion}"

        if extenstion == "":
            full_file_name = f"{file_name}"
    else:
        file_name = decrypt[0:name_len].decode()
        full_file_name = f"file.{extenstion}"

    return (decrypt, full_file_name, ext_len)
