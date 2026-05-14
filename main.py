from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import crear_tablas, get_session
from models import User
from security import hash_password, verificar_password
from pydantic import BaseModel

app = FastAPI()

@app.on_event("startup")
def on_startup():
    crear_tablas()

class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(datos: UserCreate, session: Session = Depends(get_session)):
    usuario_existe = session.exec(select(User).where(User.username == datos.username)).first()
    if usuario_existe:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    hash = hash_password(datos.password)
    nuevo_usuario = User(username=datos.username, hashed_password=hash)
    session.add(nuevo_usuario)
    session.commit()
    return {"message": "Usuario registrado exitosamente"}

@app.post("/login")
def login(datos: UserCreate, session: Session = Depends(get_session)):
    usuario = session.exec(select(User).where(User.username == datos.username)).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrecta")
    if not verificar_password(datos.password, usuario.hashed_password):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrecta")
    return {"message": "Inicio de sesión exitoso"}
