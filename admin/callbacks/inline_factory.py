from enum import StrEnum
from sys import prefix

from aiogram.filters.callback_data import CallbackData


class ActionsUpDe(StrEnum):
    select_action = "select_action"
    add = "add"
    edit = "edit"
    delete = "delete"
    confirm_delete = "confirm_delete"


class CountryCbUpDe(CallbackData, prefix="country"):
    id: int
    action: ActionsUpDe


class CityCbUpDe(CallbackData, prefix="city"):
    id: int
    action: ActionsUpDe


class DistrictCbUpDe(CallbackData, prefix="district"):
    id: int
    action: ActionsUpDe


class CountryPagination(CallbackData, prefix="country_pg"):
    page: int


class CityPagination(CallbackData, prefix="city_pg"):
    id: int
    page: int


class DistrictPagination(CallbackData, prefix="district_pg"):
    id: int
    page: int


class DistrictChangeName(CallbackData, prefix="ch_name"):
    id: int


class DistrictChangeLocation(CallbackData, prefix="ch_location"):
    id: int


class DistrictChangeNumbers(CallbackData, prefix="ch_numbers"):
    id: int

class DistrictChangeNumber(CallbackData, prefix="ch_number"):
    id: int


