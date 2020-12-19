__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = [
    "Paulo Antunes",
]
__license__ = "GPL"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


import os
import base64
from typing import Tuple
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Crypto(object):
    @staticmethod
    def _get_fkey(key: str):
        assert isinstance(key, str)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(16),
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(key.encode()))

    @staticmethod
    def encrypt(key: str, message: str) -> Tuple[str, str]:
        assert isinstance(key, str)
        assert isinstance(message, str)

        fkey = Crypto._get_fkey(key)
        f = Fernet(fkey)
        return fkey.decode(), f.encrypt(message.encode()).decode()

    @staticmethod
    def decrypt(fkey: str, encrypted_message: str) -> str:
        assert isinstance(fkey, str)
        assert isinstance(encrypted_message, str)

        f = Fernet(fkey.encode())
        return f.decrypt(encrypted_message.encode()).decode()
