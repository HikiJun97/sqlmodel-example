from sqlmodel import SQLModel, Field


class HeroTeamLink(SQLModel, table=True):
    hero_id: int | None = Field(
        default=None, primary_key=True, foreign_key="hero.id")
    team_id: int | None = Field(
        default=None, primary_key=True, foreign_key="team.id")
