from sqlalchemy import select, update, desc
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import City, District, Number, State, User


# Добавление записей
async def orm_add_user(session: AsyncSession, user_tg_id: int):
    """
    Добавляет нового пользователя, если его нет.
    """
    result = await session.execute(select(User).filter_by(user_id=user_tg_id))
    user = result.scalars().first()

    if not user:
        user = User(user_id=user_tg_id)
        session.add(user)
        await session.flush()  # Используем flush(), если транзакция уже идет

    return (
        user  # Возвращаем пользователя, независимо от того, был ли он найден или создан
    )


async def orm_add_country(
    session: AsyncSession, name_ru: str, name_en: str, name_uz: str, position: int
):
    """
    Добавляет новое государство.
    """
    state = State(name_ru=name_ru, name_en=name_en, name_uz=name_uz, position=position)
    session.add(state)
    await session.commit()


async def orm_add_city(
    session: AsyncSession, state_id: int, name_ru: str, name_en: str, name_uz: str, position: int
):
    """
    Добавляет новый город.
    """
    city = City(state_id=state_id, name_ru=name_ru, name_en=name_en, name_uz=name_uz, position=position)
    session.add(city)
    await session.commit()


async def orm_add_district_names(
    session: AsyncSession, city_id: int, name_ru: str, name_en: str, name_uz: str
):
    """
    Создаёт район с именами, но без координат.
    Возвращает ID созданного района.
    """
    district = District(
        city_id=city_id, name_ru=name_ru, name_en=name_en, name_uz=name_uz
    )
    session.add(district)
    await session.commit()
    await session.refresh(district)  # Обновляем объект, чтобы получить ID
    return district.id  # Возвращаем ID, чтобы потом обновить координаты


async def orm_add_number(session: AsyncSession, district_id: int, number: str):
    """
    Добавляет новый номер в районе.
    """
    number_obj = Number(district_id=district_id, number=number)
    session.add(number_obj)
    await session.commit()


# Получение записей
async def get_all_countryes(session: AsyncSession):
    """
    Получает список всех штатов/областей, отсортированных по position (от большего к меньшему).
    """
    stmt = select(State).order_by(desc(State.position))
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_all_cities(session: AsyncSession, state_id: int):
    """
    Получает список всех городов, отсортированных по position (от большего к меньшему).
    """
    stmt = select(City).where(City.state_id == state_id).order_by(desc(City.position))
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_all_districts(session: AsyncSession, city_id: int):
    """
    Получает список всех улиц.
    """
    stmt = select(District).where(District.city_id == city_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_districts_by_city_id(session: AsyncSession, city_id: int):
    """
    Получает список районов по ID города.
    """
    stmt = select(District).where(District.city_id == city_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_numbers_by_district_id(session: AsyncSession, district_id: int):
    """
    Получает список номеров по ID района.
    """
    stmt = select(Number).where(Number.district_id == district_id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_country_by_id(session: AsyncSession, country_id: int):
    """
    Получает штат/область по её ID.
    """
    stmt = select(State).where(State.id == country_id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def get_city_by_id(session: AsyncSession, city_id: int):
    """
    Получает город по его ID.
    """
    stmt = select(City).where(City.id == city_id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def get_district_by_id(session: AsyncSession, district_id: int):
    """
    Получает район по его ID.
    """
    stmt = select(District).where(District.id == district_id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def get_number_by_id(session: AsyncSession, number_id: int):
    """
    Получает номер по его ID.
    """
    stmt = select(Number).where(Number.id == number_id)
    result = await session.execute(stmt)
    return result.scalars().first()


async def get_language(session: AsyncSession, user_id: int):
    stmt = select(User).where(User.user_id == user_id)
    result = await session.execute(stmt)
    return result.scalars().first()


# изменение
async def orm_update_country(
    session: AsyncSession,
    country_id: int,
    name_ru: str = None,
    name_en: str = None,
    name_uz: str = None,
    position: int = None,
):
    """
    Обновляет данные о штате/области.
    """
    try:
        result = await session.execute(select(State).where(State.id == country_id))
        country = result.scalar_one()  # Получаем объект

        if name_ru is not None:
            country.name_ru = name_ru
        if name_en is not None:
            country.name_en = name_en
        if name_uz is not None:
            country.name_uz = name_uz
        if position is not None:
            country.position = position

        await session.commit()
        return country  # Можно вернуть обновленный объект

    except NoResultFound:
        return None  # Если страна не найдена


async def orm_update_city(
    session: AsyncSession,
    city_id: int,
    name_ru: str = None,
    name_en: str = None,
    name_uz: str = None,
    position: int = None,
):
    """
    Обновляет данные о городе.
    """
    try:
        result = await session.execute(select(City).where(City.id == city_id))
        city = result.scalar_one()  # Получаем объект

        if name_ru is not None:
            city.name_ru = name_ru
        if name_en is not None:
            city.name_en = name_en
        if name_uz is not None:
            city.name_uz = name_uz
        if position is not None:
            city.position = position

        await session.commit()
        return city  # Можно вернуть обновленный объект

    except NoResultFound:
        return None  # Если город не найден


async def orm_update_district_location(
    session: AsyncSession, district_id: int, latitude: float, longitude: float
):
    """
    Обновляет широту и долготу для существующего района.
    """
    stmt = (
        update(District)
        .where(District.id == district_id)
        .values(latitude=latitude, longitude=longitude)
    )
    await session.execute(stmt)
    await session.commit()


async def orm_update_district_names(
    session: AsyncSession, district_id: int, name_ru: str, name_en: str, name_uz: str
):
    """
    Обновляет названия района по ID.
    """
    try:
        result = await session.execute(
            select(District).where(District.id == district_id)
        )
        district = result.scalar_one()  # Если район не найден, выбросится NoResultFound

        district.name_ru = name_ru
        district.name_en = name_en
        district.name_uz = name_uz
        await session.commit()
        return True  # Обновление успешно

    except NoResultFound:
        return False  # Район не найден


async def orm_update_number(session: AsyncSession, number_id: int, new_number: str):
    try:
        result = await session.execute(select(Number).where(Number.id == number_id))
        number = result.scalar_one_or_none()  # Извлекаем объект

        if number is None:
            return False  # Если номера нет, возвращаем False

        number.number = new_number  # Обновляем поле
        await session.commit()
        return True

    except NoResultFound:
        return False


# удаление
async def orm_delete_country(session: AsyncSession, country_id: int):
    try:
        result = await session.execute(select(State).where(State.id == country_id))
        country = result.scalar_one()

        await session.delete(country)
        await session.commit()
        return True

    except NoResultFound:
        return False


async def orm_delete_city(session: AsyncSession, city_id: int):
    try:
        result = await session.execute(select(City).where(City.id == city_id))
        city = result.scalar_one()  # Получаем объект

        await session.delete(city)  # Удаляем объект
        await session.commit()  # Фиксируем изменения
        return True  # Удаление успешно

    except NoResultFound:
        return False  # Город не найден


async def orm_delete_district(session: AsyncSession, district_id: int):
    try:
        result = await session.execute(
            select(District).where(District.id == district_id)
        )
        district = result.scalar_one()  # Получаем объект

        await session.delete(district)  # Удаляем объект
        await session.commit()  # Фиксируем изменения
        return True  # Удаление успешно

    except NoResultFound:
        return False  # Город не найден
