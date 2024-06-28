from sqlmodel import Field, SQLModel, create_engine, Session, select
from datetime import datetime


class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    password: str = Field(max_length=30)
    role: str = Field(max_length=30)
    created_at: datetime = Field(default=datetime.utcnow)
