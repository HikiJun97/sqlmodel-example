from typing import List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from hero_team_link_model import HeroTeamLink

if TYPE_CHECKING:
    from hero_model import Hero


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    headquarters: str

    heroes: List["Hero"] = Relationship(
        back_populates="teams", link_model=HeroTeamLink)
