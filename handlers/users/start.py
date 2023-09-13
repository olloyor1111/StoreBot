from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.client.session.middlewares.request_logging import logger
from keyboards.reply.main import get_cats_markup
from loader import db

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    try:
        await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    cats = await db.select_all_cats()
    markup = get_cats_markup(cats)
    await message.answer(f"Assalomu alaykum {full_name}!", reply_markup=markup)