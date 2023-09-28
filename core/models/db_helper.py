from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.async_session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        async_session = async_scoped_session(
            session_factory=self.async_session_factory,
            scopefunc=current_task,
        )
        return async_session

    async def session_dependency(self) -> AsyncSession:
        async_session = self.get_scoped_session()

        async with async_session() as session:
            yield session
            await session.remove()
            # await async_session.remove()


db_helper = DatabaseHelper(
    url=settings.DB_URL,
    echo=settings.db_echo,
)
