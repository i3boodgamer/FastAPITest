from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from sqlalchemy.orm import sessionmaker

from core.config import settings

class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url = url,
            echo = settings.DB_ECHO,
        )
        self.session_factor = async_sessionmaker(
            bind = self.engine,
            autoflush = False,
            autocommit = False,
            expire_on_commit = False,
        )
    
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory = self.session_factor,
            scopefunc = current_task
        )
    
    async def session_despendency(self) -> AsyncSession:
        async with self.session_factor() as session:
            yield session
            await session.close()
        

db_helper = DatabaseHelper(
    url = settings.DB_URL.get_secret_value(),
    echo = settings.DB_ECHO,
)