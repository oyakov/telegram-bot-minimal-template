from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from oam import log_config
from oam.environment import DATABASE_URL, DB_CONNECTION_POOL_MIN_SIZE, DB_CONNECTION_POOL_MAX_SIZE, \
    DB_SQLACHEMY_LOGGING_ENABLED

logger = log_config.get_logger(__name__)
logger.info(f"Database URL: {DATABASE_URL}, DB_CONNECTION_POOL_MIN_SIZE: {DB_CONNECTION_POOL_MIN_SIZE}, "
            f"DB_CONNECTION_POOL_MAX_SIZE: {DB_CONNECTION_POOL_MAX_SIZE}")

sql_debug = True if DB_SQLACHEMY_LOGGING_ENABLED == 'True' else False

engine = create_async_engine(url=DATABASE_URL,
                             pool_size=int(DB_CONNECTION_POOL_MIN_SIZE),
                             max_overflow=int(DB_CONNECTION_POOL_MAX_SIZE) - int(DB_CONNECTION_POOL_MIN_SIZE),
                             echo=sql_debug)
logger.info(f"Engine created {engine}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
logger.info(f"Session generator created {SessionLocal}")


@asynccontextmanager
async def get_db():
    async with SessionLocal() as session:
        yield session



