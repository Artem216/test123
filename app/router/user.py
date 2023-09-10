from aiogram import Router
from aiogram.types import Message


router: Router = Router()


@router.message()
async def process_any_message(message: Message):
    await message.reply(text=message.text)


@router.message(commands=["start"])
async def process_start_command(message: Message):
    await message.answer(text= f"Привет, {message.from_user.first_name}! Твой аккаунт успешно привязан к боту.")

