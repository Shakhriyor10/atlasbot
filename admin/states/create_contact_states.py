from enum import StrEnum

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import State, StatesGroup


class CreateContactState(StatesGroup):
    country = State()
    city = State()
    district_info = State()
    location = State()
    contacts = State()


    

class ChoicesKeyboardAddContact(StrEnum):
    add_contacts = "Добавления контактов"
    send_news = "Рассылка новостей пользователям"
    user_contacts = "Обзор контактов"
    back = "🔙 Назад"


admin_alert = {
    "wrong": "Неверный формат!Принимает только текст, правильный вариант \n",
    "type_del_con": "Разделитель запятая",
    "type_del_district": "Разделитель ';' "
}

admin_example = {
    "help_create_country": "(пример:Узбекистан,Uzbekistan,O'zbekiston,15(номер позиции от большего к меньшему))\nСоблюдая порядок написания ру,en,уз.",
    "help_create_city": "(пример:Самарканд,Samarkand,Samarqand,15(номер позиции от большего к меньшему))\nСоблюдая порядок написания ру,en,уз.",
    "help_create_street": "(пример:Город Самарканд, ул.Абдурахман Джами 80 дом;Samarkand city, Abdurakhman Jami st., 80;Samarqand Shahar, Abdurahmon Jomiy ko'chasi, 80)\nСоблюдая порядок написания ру,en,уз.",
    "help_create_ll": "(пример:41.285277,69.262946)",
    "help_create_number": "(пример:+998912222222,+998913333333)",
}




