from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from admin.callbacks.inline_factory import (
    ActionsUpDe,
    CityCbUpDe,
    CountryCbUpDe,
    DistrictCbUpDe,
    DistrictChangeName,
    DistrictChangeLocation,
    DistrictChangeNumber,
    DistrictChangeNumbers
)

PAGE_SIZE = 8  # Количество элементов на одной странице


class Paginator:
    def __init__(self, items, page: int):
        self.items = items
        self.page = page
        self.page_size = PAGE_SIZE
        self.total_pages = (len(items) - 1) // self.page_size + 1 if items else 1

    def get_current_page_items(self):
        start = self.page * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def get_pagination_buttons(self, callback_data):
        buttons = []
        if self.page > 0:
            buttons.append(
                InlineKeyboardButton(
                    text="⬅️",
                    callback_data=callback_data(page=self.page - 1).pack(),
                )
            )
        if self.page < self.total_pages - 1:
            buttons.append(
                InlineKeyboardButton(
                    text="➡️",
                    callback_data=callback_data(page=self.page + 1).pack(),
                )
            )
        return buttons


def create_inline_callback_kb(
    lst: list[tuple[str:str]],
    last_name: str,
    last_cb: str,
    width: int = 4,
    last_button: bool = True,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    buttons = []
    for name, callback_data in lst:
        buttons.append(InlineKeyboardButton(text=name, callback_data=callback_data))

    builder.add(*buttons)
    builder.adjust(width)

    if last_button:
        builder.row(
            InlineKeyboardButton(
                text=f"Добавить {last_name}", callback_data=f"cb_add_{last_cb}"
            )
        )

    return builder.as_markup(resize_keyboard=True)


def list_location_kb(
    lst: list,
    cb_data_obj: CountryCbUpDe | CityCbUpDe | DistrictCbUpDe,
    cb_data_pg: CountryCbUpDe | CityCbUpDe | DistrictCbUpDe,
    page: int,
    cb_data_back=None,
    cnt_obj=2,
    add_country=False,
):
    paginator = Paginator(lst, page)
    page_slice = paginator.get_current_page_items()

    builder = InlineKeyboardBuilder()
    for page_object in page_slice:
        builder.button(
            text=page_object.name_ru,
            callback_data=cb_data_obj(
                id=page_object.id, action=ActionsUpDe.select_action
            ).pack(),
        )

    pagination_buttons = paginator.get_pagination_buttons(cb_data_pg)
    if pagination_buttons:
        builder.row(*pagination_buttons)

    builder.adjust(cnt_obj)

    if add_country:
        builder.row(InlineKeyboardButton(text="➕ Добавить государство", callback_data=add_country))

    if cb_data_back:
        builder.row(InlineKeyboardButton(text="🔙 Назад", callback_data=cb_data_back))

    return builder.as_markup(resize_keyboard=True)


def choise_location_kb(name: str, add_name: str, callbacks_lst: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    view_cb, add_cb, update_cb, delete_cb, back_cb = callbacks_lst
    builder.button(text=f"Связанный список {name}", callback_data=view_cb)
    builder.button(text=f"➕ Добавить {add_name}", callback_data=add_cb)
    builder.button(text="📝 Изменить ", callback_data=update_cb)
    builder.button(text="🗑️ Удалить ", callback_data=delete_cb)
    builder.button(text="🔙 Назад", callback_data=back_cb)

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def choise_district_kb(callbacks_lst: list):
    builder = InlineKeyboardBuilder()

    update_cb, delete_cb, back_cb = callbacks_lst
    builder.button(text="📝 Изменить ", callback_data=update_cb)
    builder.button(text="🗑️ Удалить ", callback_data=delete_cb)
    builder.button(text="🔙 Назад", callback_data=back_cb)

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def confirm_delete(
    callbacks_lst: list,
) -> InlineKeyboardMarkup:
    yes, no = callbacks_lst

    builder = InlineKeyboardBuilder()

    builder.button(text="Да", callback_data=yes)
    builder.button(text="Нет", callback_data=no)

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)


def change_district(district_id: int, ) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Название", callback_data=DistrictChangeName(id=district_id))
    builder.button(text="Локация", callback_data=DistrictChangeLocation(id=district_id))
    builder.button(text="Номера", callback_data=DistrictChangeNumbers(id=district_id))
    builder.button(text="🔙 Назад", callback_data=DistrictCbUpDe(id=district_id, action=ActionsUpDe.select_action))

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

def numbers_kb(numbers, district_id):
    builder = InlineKeyboardBuilder()

    for number in numbers:
        builder.button(text=number.number, callback_data=DistrictChangeNumber(id=number.id))

    builder.button(text="🔙 Назад", callback_data=DistrictCbUpDe(id=district_id, action=ActionsUpDe.edit))
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

