from sqlalchemy import inspect, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.models import Base, City, District, Number, State

# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(
    "postgresql+asyncpg://postgres:1234@localhost/atlas_express", echo=True
)

# Создаем асинхронный sessionmaker
session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def database_exists():
    """Проверяет, существуют ли все таблицы в базе данных"""
    async with engine.connect() as conn:

        def check_tables(sync_conn):
            inspector = inspect(sync_conn)
            existing_tables = inspector.get_table_names()
            return all(
                table in existing_tables for table in Base.metadata.tables.keys()
            )

        return await conn.run_sync(check_tables)


countries_data = [
    {
        "name_ru": "🇺🇿 Узбекистан",
        "name_en": "🇺🇿 Uzbekistan",
        "name_uz": "🇺🇿 O‘zbekiston",
        "cities": [
            {
                "name_ru": "Бухара",
                "name_en": "Bukhara",
                "name_uz": "Buxoro",
                "districts": [
                    {
                        "name_ru": "М.Бурханов МФЙ Каган шоссе, 180/3",
                        "name_en": "M. Burkhanov MFY Kagan Highway, 180/3",
                        "name_uz": "M. Burkhanov MFY Kagan Shosse, 180/3",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440135", "+998971470135"],
                    }
                ],
            },
            {
                "name_ru": "Кашкадарья",
                "name_en": "Kashkadarya",
                "name_uz": "Qashqadaryo",
                "districts": [
                    {
                        "name_ru": "Карши, Пахтазор МФЙ, Район Пахтазор Митти",
                        "name_en": "Karshi, Paxtazor MFY, Raion Paxtazor Mitti",
                        "name_uz": "Qarshi, Paxtazor MFY, Rayon Paxtazor Mitti",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440197", "+998971470197"],
                    },
                    {
                        "name_ru": "Шахрисабз, Напротив Арабон базара",
                        "name_en": "Shakhrisabz, Opposite the Arbon bazar",
                        "name_uz": "Shakhrisabz, Arbon bozori qarshisida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440165"],
                    },
                ],
            },
            {
                "name_ru": "Джизак",
                "name_en": "Jizzakh",
                "name_uz": "Jizzax",
                "districts": [
                    {
                        "name_ru": "Джиззак, ул.А.Навои Шох, Рядом с ArzonUz",
                        "name_en": "Jizzakh, A. Navoi Shokh st., Near ArzonUz",
                        "name_uz": "Jizzax, A. Navoi Shox ko'chasi, ArzonUz yaqinida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440193", "+998971470193"],
                    },
                    {
                        "name_ru": "Заамин, Рядом с Администрацией Зоминского района",
                        "name_en": "Zaamin, Near the Administration of Zaamin district",
                        "name_uz": "Zaamin, Zaamin tuman Administratsiyasi yaqinida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998971270193"],
                    },
                    {
                        "name_ru": "Галлаорол, ул.Мустакиллик 28",
                        "name_en": "Gallaaral, Mustaqillik st., 28",
                        "name_uz": "G'allaorol, Mustaqillik ko'chasi, 28",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998971290193"],
                    },
                ],
            },
            {
                "name_ru": "Фергана",
                "name_en": "Fergana",
                "name_uz": "Farg'ona",
                "districts": [
                    {
                        "name_ru": "ул.Ахмада Яссави 46/48",
                        "name_en": "Ahmad Yassavi st., 46/48",
                        "name_uz": "Ahmad Yassaviy ko'chasi, 46/48",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440178", "+998971470178"],
                    }
                ],
            },
            {
                "name_ru": "Маргилан",
                "name_en": "Margilan",
                "name_uz": "Marg'ilon",
                "districts": [
                    {
                        "name_ru": "Пройдя через рынок «Комбинат», находится в ряду Национального банка.",
                        "name_en": "Passing through the Kombinat market, it is located near the National Bank.",
                        "name_uz": "Kombinat bozoridan o'tib, Milliy Bankning yonida joylashgan.",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440187"],
                    }
                ],
            },
            {
                "name_ru": "Самарканд",
                "name_en": "Samarkand",
                "name_uz": "Samarqand",
                "districts": [
                    {
                        "name_ru": "ул.Абдурахман Джами 80",
                        "name_en": "Abdurahman Jami st., 80",
                        "name_uz": "Abdurahman Jomiy ko'chasi, 80",
                        "latitude": 39.65113931080511,
                        "longitude": 66.95476695804635,
                        "numbers": ["+998982770626"],
                    },
                    {
                        "name_ru": "ул.Рудаки, 277a",
                        "name_en": "Rudaki st., 277a",
                        "name_uz": "Rudakiy ko'chasi, 277a",
                        "latitude": 39.667080118294656,
                        "longitude": 66.97543711308582,
                        "numbers": ["+998950933355"],
                    },
                ],
            },
            {
                "name_ru": "Хорезм",
                "name_en": "Khorezm",
                "name_uz": "Xorazm",
                "districts": [
                    {
                        "name_ru": "Ургенч, ул.Фаязова 2/1",
                        "name_en": "Urganch, Fayazova st., 2/1",
                        "name_uz": "Urganch, Fayazova ko'chasi, 2/1",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440195", "+998971470195"],
                    },
                    {
                        "name_ru": "Беруний, Рядом с администрацией Берунийского района",
                        "name_en": "Beruniy, Near the Administration of Beruniy district",
                        "name_uz": "Beruniy, Beruniy tuman Administratsiyasi yaqinida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440194", "+998977330091"],
                    },
                    {
                        "name_ru": "Хива, Ичанкала 85-а",
                        "name_en": "Khiva, Ichanqala 85-a",
                        "name_uz": "Xiva, Ichanqola 85-a",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440189"],
                    },
                ],
            },
            {
                "name_ru": "Навои",
                "name_en": "Navoi",
                "name_uz": "Navoiy",
                "districts": [
                    {
                        "name_ru": "ул.Галаба 166-а",
                        "name_en": "Galaba st., 166-a",
                        "name_uz": "Galaba ko'chasi, 166-a",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440179", "+998971470179"],
                    },
                    {
                        "name_ru": "Зарафшан, ул.Марварид 45",
                        "name_en": "Zarafshan, Marvarid st., 45",
                        "name_uz": "Zarafshon, Marvarid ko’chasi 45",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998913389000"],
                    },
                    {
                        "name_ru": "Гиждуван",
                        "name_en": "Gijduvan",
                        "name_uz": "G'ijduvon",
                        "name_district_ru": "Фермерский рынок рядом с кафе",
                        "name_district_en": "Farmer's market near the cafe",
                        "name_district_uz": "Fermers bozor kafesi yaqinida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440146"],
                    },
                ],
            },
            {
                "name_ru": "Термез",
                "name_en": "Termez",
                "name_uz": "Termiz",
                "districts": [
                    {
                        "name_ru": "ул.Баркамол Авлод 38",
                        "name_en": "Barkamol Avlod st., 38",
                        "name_uz": "Barkamol Avlod ko'chasi, 38",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440198", "+998971470198"],
                    },
                    {
                        "name_ru": "Шеробод, ул.Мустакиллик 106",
                        "name_en": "Sherobod, Mustaqillik st., 106",
                        "name_uz": "Sherobod, Mustaqillik ko'chasi, 106",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998976979119"],
                    },
                    {
                        "name_ru": "Денов, ул.Шароф Рашидов 264",
                        "name_en": "Denov, Sharof Rashidov st., 264",
                        "name_uz": "Denov, Sharof Rashidov ko'chasi, 264",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440168"],
                    },
                ],
            },
            {
                "name_ru": "Сырдарья",
                "name_en": "Syrdarya",
                "name_uz": "Sirdaryo",
                "districts": [
                    {
                        "name_ru": "Гулистан, Обод Юрт МФЙ 3 район 17",
                        "name_en": "Gulistan, Obod Yurt MFY 3 district 17",
                        "name_uz": "Guliston, Obod Yurt MFY 3 tuman 17",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440186", "+998971470186"],
                    }
                ],
            },
            {
                "name_ru": "Кокан",
                "name_en": "Kokand",
                "name_uz": "Qo'qon",
                "districts": [
                    {
                        "name_ru": "ул.У.Носир 67",
                        "name_en": "U. Nosir st., 67",
                        "name_uz": "U. Nosir ko'chasi, 67",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440196", "+998971470196"],
                    }
                ],
            },
            {
                "name_ru": "Наманган",
                "name_en": "Namangan",
                "name_uz": "Namangan",
                "districts": [
                    {
                        "name_ru": "ул.Торагорган 165",
                        "name_en": "Toragorgan st., 165",
                        "name_uz": "Toragorgan ko'chasi, 165",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440136", "+998971470136"],
                    },
                    {
                        "name_ru": "Чорток, возле входа на рынок Наманган Питак",
                        "name_en": "Chortoq, near the entrance to the Namangan Pitak market",
                        "name_uz": "Chortoq, Namangan Pitak bozoriga kirish joyi yaqinida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998881661995"],
                    },
                ],
            },
            {
                "name_ru": "Андижан",
                "name_en": "Andijan",
                "name_uz": "Andijon",
                "districts": [
                    {
                        "name_ru": "ул.Истиклол 23",
                        "name_en": "Istiqlol st., 23",
                        "name_uz": "Istiqlol ko'chasi, 23",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440137", "+998971470137"],
                    },
                    {
                        "name_ru": "Асака, Напротив Пожарного",
                        "name_en": "Asaka, Opposite the Fire Department",
                        "name_uz": "Asaka, Yong'in bo'limi qarshisida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440172"],
                    },
                    {
                        "name_ru": "Кургантепа, У свадебного ресторана Shoxsaroy",
                        "name_en": "Kurghantepa, Near the Shoxsaroy wedding restaurant",
                        "name_uz": "Qo'rg'ontepa, Shoxsaroy to'y restorani yaqinida",
                        "latitude": 0.0,
                        "longitude": 0.0,
                        "numbers": ["+998974440175"],
                    },
                ],
            },
        ],
    },
    {
        "name_ru": "🇺🇸 США",
        "name_en": "🇺🇸 USA",
        "name_uz": "🇺🇸 AQSH",
        "cities": [
            {
                "name_ru": "Нью-Йорк",
                "name_en": "New York",
                "name_uz": "Nyu-York",
                "districts": [
                    {
                        "name_ru": "96-50 Queens Blvd, Queens, NY 11374",
                        "name_en": "96-50 Queens Blvd, Queens, NY 11374",
                        "name_uz": "96-50 Queens Blvd, Queens, NY 11374",
                        "latitude": 40.72929042581165,
                        "longitude": -73.86115454661136,
                        "numbers": ["+13472223662"],
                    },
                    {
                        "name_ru": "64-31 108th St, Queens, NY 11375",
                        "name_en": "64-31 108th St, Queens, NY 11375",
                        "name_uz": "64-31 108th St, Queens, NY 11375",
                        "latitude": 40.73214038795981,
                        "longitude": -73.84900425207988,
                        "numbers": ["+17182752203"],
                    },
                    {
                        "name_ru": "144 Highlawn Avenue Brooklyn NY USA 11223",
                        "name_en": "144 Highlawn Avenue Brooklyn NY USA 11223",
                        "name_uz": "144 Highlawn Avenue Brooklyn NY USA 11223",
                        "latitude": 40.603120898619,
                        "longitude": -73.98088383458264,
                        "numbers": ["+13152340482"],
                    },
                    {
                        "name_ru": "222 Avenue T Brooklyn NY USA 11223",
                        "name_en": "222 Avenue T Brooklyn NY USA 11223",
                        "name_uz": "222 Avenue T Brooklyn NY USA 11223",
                        "latitude": 40.59873630969586,
                        "longitude": -73.97669231478675,
                        "numbers": ["+13152340366"],
                    },
                    {
                        "name_ru": "1407 Coney Island Ave, Brooklyn, NY 11230",
                        "name_en": "1407 Coney Island Ave, Brooklyn, NY 11230",
                        "name_uz": "1407 Coney Island Ave, Brooklyn, NY 11230",
                        "latitude": 40.6233146866803,
                        "longitude": -73.96457281087486,
                        "numbers": ["+13152340366"],
                    },
                    {
                        "name_ru": "820 King Highway Brooklyn NY 11223",
                        "name_en": "820 King Highway Brooklyn NY 11223",
                        "name_uz": "820 King Highway Brooklyn NY 11223",
                        "latitude": 40.606580943745364,
                        "longitude": -73.96394979970401,
                        "numbers": ["+13152340366"],
                    },
                ],
            },
            {
                "name_ru": "Делавэр",
                "name_en": "Delaware",
                "name_uz": "Delaver",
                "districts": [
                    {
                        "name_ru": "181 Edgemoor Rd Wilmington DE 19809",
                        "name_en": "181 Edgemoor Rd Wilmington DE 19809",
                        "name_uz": "181 Edgemoor Rd Wilmington DE 19809",
                        "latitude": 39.76226451827631,
                        "longitude": -75.51355151778186,
                        "numbers": ["+13476341373"],
                    }
                ],
            },
            {
                "name_ru": "Филадельфия",
                "name_en": "Philadelphia",
                "name_uz": "Filadelfiya",
                "districts": [
                    {
                        "name_ru": "1619 Grant Ave STORE 18-19, Philadelphia, PA 19115",
                        "name_en": "1619 Grant Ave STORE 18-19, Philadelphia, PA 19115",
                        "name_uz": "1619 Grant Ave STORE 18-19, Philadelphia, PA 19115",
                        "latitude": 40.08525751201282,
                        "longitude": -75.0362791946709,
                        "numbers": ["+12673512222"],
                    }
                ],
            },
        ],
    },
]

async def populate_db():
    async with session_maker() as session:
        try:
            for country_data in countries_data:
                state = State(
                    name_ru=country_data["name_ru"],
                    name_en=country_data["name_en"],
                    name_uz=country_data["name_uz"],
                )
                session.add(state)
                await session.flush()  # Получаем ID

                print(f"Добавляем государство: {state.name_ru}")

                for city_data in country_data["cities"]:
                    city = City(
                        name_ru=city_data["name_ru"],
                        name_en=city_data["name_en"],
                        name_uz=city_data["name_uz"],
                        state_id=state.id,
                    )
                    session.add(city)
                    await session.flush()

                    print(f"  Добавляем город: {city.name_ru}")

                    for district_data in city_data["districts"]:
                        district = District(
                            name_ru=district_data["name_ru"],
                            name_en=district_data["name_en"],
                            name_uz=district_data["name_uz"],
                            latitude=district_data["latitude"],
                            longitude=district_data["longitude"],
                            city_id=city.id,
                        )
                        session.add(district)
                        await session.flush()

                        print(f"    Добавляем район: {district.name_ru}")

                        for number in district_data["numbers"]:
                            number_entry = Number(number=number, district_id=district.id)
                            session.add(number_entry)

                        print(f"      Добавляем номера: {[num for num in district_data['numbers']]}")

            await session.commit()

        except Exception as e:
            await session.rollback()
            print(f"Ошибка при добавлении данных: {e}")



async def create_db():
    """Создает базу данных и добавляет предустановленные государства."""
    if not await database_exists():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        # Открываем сессию и добавляем данные
        await populate_db()
    else:
        print("База данных уже существует, создание не требуется.")


# Пример вызова функций
if __name__ == "__main__":
    import asyncio

    asyncio.run(create_db())
