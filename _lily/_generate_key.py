


def generate_key(password: str, salt: None | bytes = None):
    import base64
    import hashlib
    from os import urandom

    from cryptography.fernet import Fernet

    if salt == None:
        _salt = urandom(16)
    else:
        _salt = salt

    key = hashlib.pbkdf2_hmac(
		"sha256",
		password.encode(),
		_salt,
		600000
	)

    key = base64.urlsafe_b64encode(key)

    fern = Fernet(key)


    return (_salt, fern)
