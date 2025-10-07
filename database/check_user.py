from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


class Request:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user_id: int, language: str):
        async with self.session.begin():
            result = await self.session.execute(
                select(User).where(User.user_id == user_id)
            )
            user = result.scalar_one_or_none()

            if user:
                if user.language != language:  # Обновляем язык только при изменении
                    user.language = language
            else:
                new_user = User(user_id=user_id, language=language, is_active=True)
                self.session.add(new_user)

            await self.session.commit()  # Добавляем коммит

    async def change_language(self, user_id: int, lang):
        async with self.session.begin():  # Добавляем контекст транзакции
            stmt = update(User).where(User.user_id == user_id).values(language=lang)
            await self.session.execute(stmt)

    async def get_active_users(self):
        """Получить список всех активных пользователей."""
        result = await self.session.execute(
            select(User.user_id).where(User.is_active == True)
        )
        return list(result.scalars().all())

    async def disable_user(self, user_id: int):
        """Отключить пользователя, если он заблокировал бота."""
        async with self.session.begin():
            result = await self.session.execute(
                select(User).where(User.user_id == user_id)
            )
            user = result.scalar_one_or_none()
            if user:
                user.is_active = False
                await self.session.commit()
