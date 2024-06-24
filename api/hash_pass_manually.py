import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256( password.encode() ).hexdigest()


password = "brs1911"
hashed_password = hash_password( password )
print( hashed_password )
