from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile
from aiogram.fsm.context import FSMContext

from states import MenuOption

from database import get_filter_products, get_category_by_id

from texts import (
    GENDER_TEXT, START_TEXT, CATEGORY_TEXT, 
    SEASON_TEXT, menu_oxiri)
from keyboards import (
    GENDER_KEYBOARD_MENU, REGISTER_END_KEYBOARD, 
    category_button, SEASON_KEYBOARD)

from deep_translator import GoogleTranslator


user_router = Router()

@user_router.message(F.text == "Menu")
async def start_menu(message:Message, state:FSMContext):
    image_path = "media/image/main.jpg"
    await message.answer("Siz menu tanladingiz",reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=FSInputFile(path=image_path),caption=GENDER_TEXT, reply_markup=GENDER_KEYBOARD_MENU)
    await state.set_state(MenuOption.gender)
    

@user_router.callback_query(F.data.startswith("menu_gender_"))
async def get_gender_menu(cal:CallbackQuery,state:FSMContext):
    gender = cal.data.split("_")[-1]

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
        category_id = data["category"]

        await state.clear()
        await cal.message.edit_reply_markup(reply_markup=None)
        await cal.message.edit_caption(caption=None)

        category_name = get_category_by_id(category_id)[0]

        await cal.message.answer(menu_oxiri(gender,category_name,season))
        data = get_filter_products(category_id, season,gender)

        jins = GoogleTranslator(source= "auto", target="uz").translate(gender)
        turi = GoogleTranslator(source= "auto", target="uz").translate(category_name)
        fasl = GoogleTranslator(source= "auto", target="uz").translate(season)
        r = ""
        for i in range(len(turi)):
            if i == 2:
                r+=turi[i].upper()
            else:
                r+=turi[i]

        for product in data:
            product_text = f"""
            {product[1]}
            👕 Kategoriya: {r}
            💰 Narxi: {product[3]} so‘m
            📏 O‘lcham: {product[5]}
            👤 Kim uchun: {jins.title()}
            🌤 Fasl: {fasl.title()}
            🏷 Brend: {product[8]}
            📦 Omborda: {product[4]} dona mavjud
            """
            tarjima = GoogleTranslator(source="auto", target="uz").translate(product_text)

            await cal.message.answer(text=tarjima)
        
