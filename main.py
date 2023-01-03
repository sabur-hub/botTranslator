import os
# import types
# from youtube_search import YoutubeSearch
# import hashlib
import googletrans
from aiogram import Bot, Dispatcher, executor, types
import logging
# from aiogram.types.message import ContentType
# from aiogram.types.message import ContentTypes
from config import Bot_token
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from googletrans import *
# import pyttsx3
from gtts import gTTS

# import time
logging.basicConfig(level=logging.INFO)

translator = googletrans.Translator()

bot = Bot(Bot_token)
dp = Dispatcher(bot)

# mainMenu = InlineKeyboardMarkup(row_width=2)
# btnMenu = InlineKeyboardButton(text='RU', callback_data='btnMenu')
# btnMenu1 = InlineKeyboardButton(text='RU', callback_data='btnMenu')
# btnMenu2 = InlineKeyboardButton(text='RU', callback_data='btnMenu')
# btnMenu3 = InlineKeyboardButton(text='RU', callback_data='btnMenu')
# btnMenu4 = InlineKeyboardButton(text='RU', callback_data='btnMenu')

# mainMenu.insert(btnMenu)
# mainMenu.insert(btnMenu1)
# mainMenu.insert(btnMenu2)
# mainMenu.insert(btnMenu3)
# mainMenu.insert(btnMenu4)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'I can translate every thiks'
                                    'write your text')


@dp.message_handler()
async def type_search(message: types.Message):
    translate = translator.translate(message.text, dest='ru')
    await bot.send_message(message.chat.id, translate.text)
    voice = gTTS(translate.text, lang='ru')
    d = r'C:\Student life and project\project\tg _bot\translater\voice\audio.mp3'
    voice.save(d)
    AUDIO_PATH = os.path.expanduser(r'C:\Student life and project\project\tg _bot\translater\voice\audio.mp3')
    audio = types.InputFile(AUDIO_PATH)
    await message.reply_audio(audio=audio, title='r')


if __name__ == '__main__':
    executor.start_polling(dp)
