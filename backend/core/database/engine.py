from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel

async_engine = None


async def create_tables(async_engine: AsyncEngine):
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await async_engine.dispose()
