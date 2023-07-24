from aiogram import F
from aiogram import Router
from aiogram.types import CallbackQuery


router: Router = Router()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed' или 'big_button_2_pressed'
@router.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    # проверка на текст самого сообщения, которое редактируется
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup)
    await callback.answer()


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@router.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    # проверка на текст самого сообщения, которое редактируется
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup)
    await callback.answer()


@router.callback_query(F.data == 'big_button_3_pressed')
async def process_button_3_press(callback: CallbackQuery):
    # проверка на текст самого сообщения, которое редактируется
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 3':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 3',
            reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 3')


@router.callback_query(F.data == 'big_button_4_pressed')
async def process_button_4_press(callback: CallbackQuery):
    # проверка на текст самого сообщения, которое редактируется
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 4':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 4',
            reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 4', show_alert=True)
