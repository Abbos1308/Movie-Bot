from simple_header import get
from time import sleep

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
import logging,re
from aiogram import types
from aiogram.types import CallbackQuery , InputFile

from .download import download_file
from data.config import ADMINS , CHANNEL_ID
from filters import IsUser, IsSuperAdmin, IsGuest
from filters.admins import IsAdmin
from keyboards.inline.main_menu_super_admin import main_menu_for_super_admin, main_menu_for_admin
from loader import dp, db, bot


logging.basicConfig(level=logging.INFO)
import re,json
#from tiktok_downloader import snaptik
import os, requests

import random  
import os





@dp.message_handler(IsAdmin(), CommandStart(), state="*")
async def bot_start_admin(message: types.Message):
    await message.answer(f"Salom admin, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_admin)

@dp.message_handler(IsSuperAdmin(), CommandStart(), state="*")
async def bot_start_super_admin(message: types.Message):
    await message.answer(f"Salom boss, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_super_admin)

@dp.message_handler(commands=['start'], state="*")
async def bot_start(message: types.Message):
    user = message.from_user
    try:
        db.add_user(user_id=user.id,name=user.first_name,active=1)
    except:
        pass
    user_id = message.from_user.first_name
    await message.answer("""
    Salom! 👋
Men sizga qidirgan kinoingizni topishda yordam beradigan botman. 🎥

Qanday foydalaniladi?
1️⃣ Kodni kiriting (masalan, 6).
2️⃣ Shu zahotiyoq o‘sha kodga mos kinoni sizga yuboraman.


Tayyor bo‘lsangiz, boshlang! 🔎

🎬 Sizning kino yordamchingiz:
👉 @SizningBotingizNomi


""",parse_mode="HTML")


  
# Handle text messages
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    
    try:
        post_id = int(message.text)  # Foydalanuvchi yuborgan raqam
        # Kanaldagi kerakli postni olish
        post = await bot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=post_id)
        if not post:
            await message.reply("Bunday kod bilan kino mavjud emas.Kino oʻchirib yuborilgan boʻlishi mumkin!")
    except Exception as e:
        await message.reply(f"Xato yuz berdi! Qayta urining.")
