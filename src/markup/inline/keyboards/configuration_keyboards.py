from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def config_action_selector():
    inline_btn_1 = InlineKeyboardButton(text='Настройка групп', callback_data='config_groups')
    inline_btn_2 = InlineKeyboardButton(text='Дополнительные настройки', callback_data='config_misc')
    return InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1, inline_btn_2]])


def config_group_action_selector():
    inline_btn_1 = InlineKeyboardButton(text='Добавить группу', callback_data='config_groups_add')
    inline_btn_2 = InlineKeyboardButton(text='Редактировать список групп', callback_data='config_groups_list')
    inline_btn_3 = InlineKeyboardButton(text='Назад', callback_data='config_back')
    return InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1, inline_btn_2, inline_btn_3]])


def config_back():
    inline_btn_1 = InlineKeyboardButton(text='Назад', callback_data='config_back')
    return InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1]])


def config_misc_action_selector():
    inline_btn_1 = InlineKeyboardButton(text='NOT IMPLEMENTED', callback_data='config_misc_1')
    inline_btn_2 = InlineKeyboardButton(text='NOT IMPLEMENTED', callback_data='config_misc_2')
    inline_btn_3 = InlineKeyboardButton(text='Назад', callback_data='config_back')
    return InlineKeyboardMarkup(inline_keyboard=[[inline_btn_1, inline_btn_2, inline_btn_3]])
