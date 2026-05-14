from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./usuarios.db"

engine = create_engine(DATABASE_URL)

def crear_tablas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

  