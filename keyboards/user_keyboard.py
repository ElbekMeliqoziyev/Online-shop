from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton)

from database import get_category


GENDER_KEYBOARD_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Male", callback_data="menu_gender_male")],
        [InlineKeyboardButton(text="Female", callback_data="menu_gender_female")],
        [InlineKeyboardButton(text="Child", callback_data="menu_gender_child")],
        [InlineKeyboardButton(text="Cancel", callback_data="menu_gender_cancel")]
    ]
)

def category_button():
    inline_keyboard = []
    button = []
    data = get_category()

    for i in range(1,len(data)+1):
        button.append(InlineKeyboardButton(text=data[i][1], callback_data=f"category_{data[i][0]}"))
        if i%2 == 0:
            inline_keyboard.append(button)
            button = []

        if button:
            inline_keyboard.append(button)

    inline_keyboard.append([InlineKeyboardButton(text="🔙 Back", callback_data="category_back")])  

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    ) 

CATEGORY_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👔 Shirt", callback_data="category_shirt"),
        InlineKeyboardButton(text="👟 Shoes", callback_data="category_shoes"),
    ],
    [
        InlineKeyboardButton(text="🧢 Cap", callback_data="category_cap"),
        InlineKeyboardButton(text="🧥 Jacket", callback_data="category_jacket"),
    ],
    [
        InlineKeyboardButton(text="👖 Trousers", callback_data="category_trousers"),
        InlineKeyboardButton(text="💼 Suit", callback_data="category_suit"),
    ],
    [
        InlineKeyboardButton(text="🕶️ Accessory", callback_data="category_accessory"),
        InlineKeyboardButton(text="🎒 Bag", callback_data="category_bag"),
    ],
    [
        InlineKeyboardButton(text="🔙 Back", callback_data="category_back"),
    ]
])

SEASON_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🌸 Bahor", callback_data="season_spring"),
        InlineKeyboardButton(text="☀️ Yoz", callback_data="season_summer"),
    ],
    [
        InlineKeyboardButton(text="🍂 Kuz", callback_data="season_autumn"),
        InlineKeyboardButton(text="❄️ Qish", callback_data="season_winter"),
    ],
    [
        InlineKeyboardButton(text="⛅ All Season", callback_data="season_all"),
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data="season_back"),
    ]
])