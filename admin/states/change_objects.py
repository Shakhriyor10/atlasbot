from aiogram.fsm.state import State, StatesGroup


class ChangeObject(StatesGroup):
    country_change = State()
    city_change = State()
    name_change_district = State()
    location_change_district = State()
    number_change_district = State()


    