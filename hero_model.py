from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
from hero_team_link_model import HeroTeamLink

if TYPE_CHECKING:
    from team_model import Team


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    teams: List["Team"] | None = Relationship(
        back_populates="heroes", link_model=HeroTeamLink
    )
