from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine, Session, select
from datetime import datetime
from contextlib import asynccontextmanager

from models import User
from engine import engine

engine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine
    db_url: str = f"mysql+pymysql://sgn04088:whgudwns1997@localhost:3306/test"
    engine = create_engine(db_url, echo=True)
    yield
    engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/users/")
def read_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


@app.get("/user/{user_id}")
def read_user(user_id: str):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user


@app.post("/user/", response_model=User)
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    with Session(engine) as session:
        user = session.get(User, user_id)
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully"}


@app.get("/")
def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
