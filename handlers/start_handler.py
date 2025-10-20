from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from states import Register

from texts import START_TEXT
from keyboards import (
    START_KEYBOARD, PHONE_KEYBOARD,
    GENDER_KEYBOARD, ADDRESS_KEYBOARD,
    REGISTER_END_KEYBOARD
)

from database import register_by_id, insert_user

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message:Message):
    if register_by_id(message.from_user.id):
        await message.answer(START_TEXT, reply_markup= REGISTER_END_KEYBOARD)
    else:
        await message.answer(START_TEXT, reply_markup = START_KEYBOARD)

@start_router.message(F.text == "Register")
async def register_handler(message:Message, state:FSMContext):
    await state.set_state(Register.name)
    await message.answer("Ism-Familiyangizni kiriting:", reply_markup=ReplyKeyboardRemove())

@start_router.message(Register.name)
async def get_name(message:Message, state:FSMContext):
    full_name = message.text
    if full_name.isalpha():
        await message.answer("Ism qabul qilindi, Telefon raqam yozing (+998901234567)", reply_markup=PHONE_KEYBOARD)
        await state.update_data(name = message.text)
        await state.set_state(Register.phone)
    else:
        await message.answer("Ismni to'g'ri formatda yozing")
    

@start_router.message(Register.phone)
async def get_phone(message:Message, state:FSMContext):
    if message.contact:
        phone = message.contact.phone_number
        await message.answer(f"Raqam {phone} qabul qilindi", reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Jins tanlang:", reply_markup=GENDER_KEYBOARD)
        await state.update_data(phone = phone)
        await state.set_state(Register.gender)
        
    else:
        phone = message.text
        await state.update_data(phone = phone)
        await state.set_state(Register.gender)
        await message.answer(f"Raqam {phone} qabul qilindi", reply_markup=ReplyKeyboardRemove())
        await message.answer(f"Jins tanlang:", reply_markup=GENDER_KEYBOARD)

@start_router.callback_query(F.data.startswith("gender_"))
async def get_gender(cal:CallbackQuery, state:FSMContext):
    gender = cal.data.split("_")[-1]
    await state.update_data(gender = gender)
    await state.set_state(Register.address)
    await cal.message.answer(f"Siz {gender}ni tanladingiz", reply_markup=ADDRESS_KEYBOARD)



@start_router.message(Register.address)
async def get_address(message:Message, state:FSMContext):
    if message.location:
        lon = message.location.longitude
        lat = message.location.latitude
        data = await state.get_data()
        await state.clear()
        fullname = data.get("name")
        phone = data.get("phone")
        gender = data.get("gender")
        address = f"lon: {lon}, lat: {lat}"

        if insert_user(fullname,phone,gender,address, message.from_user.id):
            await message.answer("Siz ro'yxatdan o'tdingiz", reply_markup = REGISTER_END_KEYBOARD)
        else:
            await message.answer("Ro'yxatdan o'tishda qandaydir muammo bor, qayta urinib ko'ring", reply_markup= ReplyKeyboardRemove())
    else:
        await message.answer("Tugmachani bosing")
