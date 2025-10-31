from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.fsm.context import FSMContext

from states import MenuOption

from database import get_filter_products, get_category_by_name

from texts import (
    GENDER_TEXT, START_TEXT, CATEGORY_TEXT, 
    SEASON_TEXT, menu_oxiri)
from keyboards import (
    GENDER_KEYBOARD_MENU, REGISTER_END_KEYBOARD, 
    category_button, SEASON_KEYBOARD)

user_router = Router()

@user_router.message(F.text == "Menu")
async def start_menu(message:Message, state:FSMContext):
    image_path = "media/image/main.jpg"
    await message.answer("Siz menu tanladingiz",reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=FSInputFile(path=image_path),caption=GENDER_TEXT, reply_markup=GENDER_KEYBOARD_MENU)
    await state.set_state(MenuOption.gender)
    

@user_router.callback_query(F.data.startswith("menu_gender_"))
async def get_gender_menu(cal:CallbackQuery,state:FSMContext):
    gender = cal.data.split("_")[-1].title()

    await cal.answer()

    if gender == "Cancel":
        await state.clear()
        await cal.message.answer("Cancel")
        await cal.message.edit_reply_markup(reply_markup=None)
        await cal.message.answer(START_TEXT, reply_markup=REGISTER_END_KEYBOARD)
    else:
        await cal.message.edit_reply_markup(reply_markup=None)
        await cal.message.edit_caption(caption=CATEGORY_TEXT, reply_markup=category_button())
        await state.update_data(gender = gender)
        await state.set_state(MenuOption.category)

@user_router.callback_query(F.data.startswith("category_"))
async def get_category(cal:CallbackQuery, state:FSMContext):
    category = cal.data.split("_")[-1]

    await cal.answer()

    if category == "back":
        await cal.message.edit_caption(caption=GENDER_TEXT)
        await cal.message.edit_reply_markup(reply_markup=GENDER_KEYBOARD_MENU)
    else:
        await cal.message.edit_reply_markup(reply_markup=None)
        await cal.message.edit_caption(caption=SEASON_TEXT, reply_markup=SEASON_KEYBOARD)
        await state.update_data(category = category)
        await state.set_state(MenuOption.season)

@user_router.callback_query(F.data.startswith("season_"))
async def get_season(cal:CallbackQuery, state:FSMContext):
    season = cal.data.split("_")[-1]

    await cal.answer()

    if season == "back":
        await cal.message.edit_caption(caption=CATEGORY_TEXT)
        await cal.message.edit_reply_markup(reply_markup=category_button())
    else:
        data = await state.get_data()
        gender = data["gender"]
        category = data["category"]

        await state.clear()
        await cal.message.edit_reply_markup(reply_markup=None)
        await cal.message.edit_caption(caption=None)
        await cal.message.answer(menu_oxiri(gender,category,season))

        category_id = get_category_by_name(category)[0]
        baza = get_filter_products(category_id, season,gender)
        
