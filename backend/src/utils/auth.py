import hashlib
import os
from jose import jwt
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

import hashlib
import os

from src.config import APP_SECRET

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

def verify_password(plain_password, hashed_password, salt):
    salt_bytes = bytes.fromhex(salt)
    peppered_password = plain_password.encode() + APP_SECRET.encode()   
    pwdhash = hashlib.pbkdf2_hmac('sha256', peppered_password, salt_bytes, 100000)
    return pwdhash.hex() == hashed_password

def create_access_token(data: dict):
    to_encode = data.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "iat:": round(now.timestamp()),
        "exp": round(expire.timestamp())
    })
    encoded_jwt = jwt.encode(to_encode, APP_SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def hash_password(password: str) -> (str, str): # type: ignore
    """Hash a password using both a salt and a pepper."""
    # Generate a random salt
    salt = os.urandom(16)  # 128-bit salt
    # Encode and concatenate password with pepper
    peppered_password = password.encode() + APP_SECRET.encode()
    # Hash the peppered password with the salt using PBKDF2
    pwdhash = hashlib.pbkdf2_hmac('sha256', peppered_password, salt, 100000)
    # Convert salt and hash to hexadecimal format for storage
    salt_hex = salt.hex()
    pwdhash_hex = pwdhash.hex()
    return pwdhash_hex, salt_hex

def encrypt(data: str) -> str:
	return Fernet(APP_SECRET).encrypt(data.encode()).decode()

def decrypt(data: str) -> str:
	return Fernet(APP_SECRET).decrypt(data.encode()).decode()