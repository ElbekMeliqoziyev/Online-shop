from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton)

START_KEYBOARD = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text="Register"), KeyboardButton(text="Menu")],
        [KeyboardButton(text="Orders"), KeyboardButton(text="Contact")]
    ],
    resize_keyboard = True
)



REGISTER_END_KEYBOARD = ReplyKeyboardMarkup(
    keyboard = [
        [ KeyboardButton(text="Menu")],
        [KeyboardButton(text="Orders") ],
        [KeyboardButton(text="Contact")]
    ],
    resize_keyboard = True
)



PHONE_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Phone", request_contact=True)]
    ],
    resize_keyboard=True
)



GENDER_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Male", callback_data="gender_male"),
            InlineKeyboardButton(text="Female", callback_data="gender_female")
         ]
    ]
)



ADDRESS_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Address")]
    ],
    resize_keyboard=True
)