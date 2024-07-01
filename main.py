from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)
from hero_model import Hero
from team_model import Team


async def create_table(async_engine: AsyncEngine):
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
    await async_engine.dispose()


async def main(async_engine):
    await create_table(async_engine)
    async_session = async_sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session.begin() as asession:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers]
        )
        asession.add(hero_deadpond)
        asession.add(hero_rusty_man)
        asession.add(hero_spider_boy)

        # Heroes' IDs are not printed here because they are not committed yet.
        # print("Deadpond:", hero_deadpond)
        # print("Deadpond teams:", hero_deadpond.teams)
        # print("Rusty-Man:", hero_rusty_man)
        # print("Rusty-Man Teams:", hero_rusty_man.teams)
        # print("Spider-Boy:", hero_spider_boy)
        # print("Spider-Boy Teams:", hero_spider_boy.teams)

        # Committing is executed automatically when the async with block is exited.
        # await asession.commit()

    # Heroes' IDs are printed here because they are committed.
    # To print the instances, expire_on_commit must be False.
    print("Deadpond:", hero_deadpond)
    print("Deadpond teams:", hero_deadpond.teams)
    print("Rusty-Man:", hero_rusty_man)
    print("Rusty-Man Teams:", hero_rusty_man.teams)
    print("Spider-Boy:", hero_spider_boy)
    print("Spider-Boy Teams:", hero_spider_boy.teams)

    await async_engine.dispose()


if __name__ == "__main__":
    import asyncio

    async_engine = create_async_engine(
        "mysql+aiomysql://sgn04088:whgudwns1997@localhost/sqlmodel", echo=True
    )

    asyncio.run(main(async_engine))
