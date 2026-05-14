import bcrypt
import os 
from dotenv import load_dotenv

load_dotenv()

PEPPER = os.getenv("PEPPER")

def hash_password(password: str):
    password_pepper = password + PEPPER
    pass_bytes = password_pepper.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pass_bytes, salt)
    return hash.decode('utf-8')

def verificar_password(password: str, hashed_password: str) -> bool:
    password_pepper = password + PEPPER
    pass_bytes = password_pepper.encode('utf-8')
    hash_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(pass_bytes, hash_bytes)

 
