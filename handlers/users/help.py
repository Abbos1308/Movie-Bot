from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

#Dasturchi @Mrgayratov kanla @Kingsofpy
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("""
    Yordam! 🆘
Men sizga kino topishda yordam berishga tayyorman.

Qanday foydalanish kerak?
1️⃣ Kinoning kodini kiriting (masalan, 56).
2️⃣ Men sizga shu kodga mos kinoni yuboraman.

Agar boshqa savollar bo‘lsa yoki yordam kerak bo‘lsa, bu xabarni qayta yuboring.

Bot bilan ishlashni boshlash uchun kodni kiriting! 🔍

🎬 Sizning kino yordamchingiz:
👉 @SizningBotingizNomi""")
    
    await message.answer("\n".join(text))
