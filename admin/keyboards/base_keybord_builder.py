from typing import Iterable

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def base_kb_builder(iter_choices: Iterable, num_size_kb: int=2) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for item in iter_choices:
        builder.button(text=item)

    builder.adjust(num_size_kb)
    return builder.as_markup(resize_keyboard=True)
