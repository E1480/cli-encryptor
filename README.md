# cli-encryptor

A simple Python command-line tool for encrypting and decrypting text and files with a password, built on [Fernet](https://cryptography.io/en/latest/fernet/) from the `cryptography` library.

> [!WARNING]
> **This project is just for fun.** It's a hobby project made for learning and experimenting. Please don't use it to protect anything important or sensitive.

## Features

- Encrypt and decrypt plain text strings
- Encrypt and decrypt files
- Optionally preserve the original file name inside the encrypted file
- Choose the name of the encrypted output file
- Rename the output file when decrypting

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) (recommended; the repo includes a `uv.lock`)

Dependencies (installed automatically):

- [`cryptography`](https://pypi.org/project/cryptography/)
- [`typer`](https://pypi.org/project/typer/)

## Installation

```bash
git clone https://github.com/E1480/cli-encryptor.git
cd cli-encryptor
uv sync
```

Without uv:

```bash
pip install cryptography typer
```

## Usage

The tool has two commands: `encrypt` and `decrypt`. Both take the target and a password as positional arguments.

```bash
uv run app.py encrypt TARGET PASSWORD [OPTIONS]
uv run app.py decrypt TARGET PASSWORD [OPTIONS]
```

(If you installed with pip, use `python app.py ...` instead of `uv run app.py ...`.)

### Encrypt

| Option | Short | Description |
| --- | --- | --- |
| `--file` | `-f` | Treat `TARGET` as a file path instead of text |
| `--preserve` | `-p` | Preserve the original file name inside the encrypted file |
| `--out_name` | `-o` | Name of the output file (default: `file.enc`) |

### Decrypt

| Option | Short | Description |
| --- | --- | --- |
| `--file` | `-f` | Treat `TARGET` as a file path instead of text |
| `--rename` | `-r` | Rename the decrypted output file |

## Examples

**Encrypt and decrypt text**

```bash
uv run app.py encrypt "my secret message" "my-password"
uv run app.py decrypt "<encrypted text>" "my-password"
```

**Encrypt a file**

```bash
uv run app.py encrypt notes.txt "my-password" --file
```

**Encrypt a file, keep its name, and choose the output name**

```bash
uv run app.py encrypt notes.txt "my-password" -f -p -o notes.enc
```

**Decrypt a file**

```bash
uv run app.py decrypt notes.enc "my-password" --file
```

**Decrypt a file and rename the result**

```bash
uv run app.py decrypt notes.enc "my-password" -f -r notes_restored.txt
```

To see all options at any time:

```bash
uv run app.py --help
uv run app.py encrypt --help
```

## Security notes

- Passing a password as a command-line argument can expose it in your shell history and in process listings. Avoid using this tool with sensitive passwords on shared machines.
- Keep your password safe. Encrypted data cannot be recovered without it.
- This is a small personal project and has not been independently audited. For high-stakes data, use a well-established tool.

## Project structure

```
cli-encryptor/
├── app.py            # CLI entry point (Typer commands)
├── _lily/            # Encryption and decryption logic
├── pyproject.toml    # Project metadata and dependencies
├── uv.lock           # Locked dependency versions
└── LICENSE           # MIT License
```

## License

This project is licensed under the [MIT License](LICENSE).
