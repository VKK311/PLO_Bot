import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from PIL import Image
import pytesseract
import io

API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hello! Send me an image and I'll extract the text!")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_docs_photo(message: types.Message):
    photo = message.photo[-1]
    photo_bytes = await photo.download(destination=io.BytesIO())
    photo_bytes.seek(0)
    image = Image.open(photo_bytes)

    text = pytesseract.image_to_string(image)
    await message.answer(f"Here is the extracted text:\n\n{text}")

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
