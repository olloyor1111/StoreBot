from aiogram import Router, types, F
from states.store import StoreStates
from aiogram.fsm.context import FSMContext
from loader import db
from utils.misc.extra import get_cart_detail_text, get_total_price
from keyboards.reply.main import phone_markup, get_location
from keyboards.reply.main import get_cats_markup

router = Router()

@router.message(F.text == "🛒 Rasmiylashtirish")
async def confirm_order(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    if user:
        cart = await db.select_cart(user_id=user["id"])
        cart_items = await db.select_cart_items(cart_id=cart["id"])
        if cart_items:
            text = await get_cart_detail_text(cart_items=cart_items)
            await message.answer(text)
            await message.answer("Buyurtmani tasdiqlash uchun telefon raqamingizni jo'nating", reply_markup=phone_markup())
            await state.set_state(StoreStates.confirm)


@router.message(StoreStates.confirm, F.contact)
async def get_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data({"phone_number": phone_number})
    await message.answer("Raqamingiz saqlandi, endi joriy joylashuvni jo'nating", reply_markup=get_location())


@router.message(StoreStates.confirm, F.location)
async def get_live_location(message: types.Message, state: FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    data = await state.get_data()
    phone_number = data.get("phone_number")
    cats = await db.select_all_cats()
    markup = get_cats_markup(cats)
    # save order
    user = await db.select_user(telegram_id=message.from_user.id)
    cart = await db.select_cart(user_id=user["id"])
    cart_items = await db.select_cart_items(cart_id=cart["id"])
    total_price = await get_total_price(cart_items=cart_items)
    await db.add_order(user_id=user["id"], paid=False, total_price=total_price, lat=lat, lon=lon, phone_number=phone_number)

    # get_last_order
    order = await db.select_order(user_id=user["id"], paid=False, total_price=total_price)
    for cart_item in cart_items:
        product = await db.select_product(id=cart_item["product_id"])
        await db.add_order_item(order_id=order["id"], product_id=cart_item["product_id"], quantity=cart_item["quantity"], price=product["price"])
        await db.clear_cart(cart_id=cart["id"])
    await message.answer("✅ Barcha ma'lumotlar saqlandi, endi to'lov qilishingiz kerak!", reply_markup=markup)
    await state.set_state(StoreStates.category)
