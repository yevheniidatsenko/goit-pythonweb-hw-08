from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.conf.config import settings

# Asynchronous URL for connecting to PostgreSQL
SQLALCHEMY_DATABASE_URL = settings.database_url.replace("postgresql://", "postgresql+asyncpg://")

# Asynchronous engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Asynchronous session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

# Dependency for getting an asynchronous session
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session