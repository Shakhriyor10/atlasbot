import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection
from alembic import context

# Импорт моделей
from database.models import Base  # Укажи правильный путь к Base

# Настройки логов
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


# Создаём асинхронный движок
connectable = create_async_engine(
    config.get_main_option("sqlalchemy.url"),
    poolclass=pool.NullPool,
)


async def run_migrations_online():
    """Запускаем миграции в 'онлайн' режиме с асинхронным движком."""
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

def do_run_migrations(connection: AsyncConnection):
    """Выполняем миграции в контексте подключения."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

# Запускаем миграции асинхронно
asyncio.run(run_migrations_online())

