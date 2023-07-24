from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.keyboards import main_inline

router: Router = Router()


@router.message(Command("menu_inline"))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.username}!', reply_markup=main_inline.keyboard)
    # await message.answer(text=LEXICON_RU['/start'])
