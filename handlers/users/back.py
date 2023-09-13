from aiogram import Router, types, F
from states.store import StoreStates
from keyboards.reply.main import get_cats_markup
from aiogram.fsm.context import FSMContext
from loader import db

router = Router()


@router.message(StoreStates.category, F.text == "⬅️ Orqaga")
async def back_previous_state(message: types.Message, state: FSMContext):
    data = await state.get_data()
    parent_id = data.get("parent_id")
    if parent_id:
        category = await db.select_category(id=parent_id)
        await state.update_data({"parent_id": category["parent_id"]})
        cats = await db.select_cats_by_parent_id(parent_id=parent_id)
        await message.answer(f"Oldingi bo'limga qaytdingiz", reply_markup=get_cats_markup(cats=cats, back=True))
    else:
        cats = await db.select_all_cats()
        await message.answer(f"Asosiy bo'limga qaytdingiz", reply_markup=get_cats_markup(cats=cats))