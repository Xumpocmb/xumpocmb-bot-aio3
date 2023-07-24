# import requests
# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from tgbot.config import load_config
# from tgbot.misc.states import WeatherStatesGroup
#
# from tgbot.keyboards.user_keyboard import keyboard_cancel
# from tgbot.keyboards.user_keyboard import keyboard
#
#
# config = load_config(".env")
# API = config.weather.token
#
#
# async def cmd_cancel(message: types.Message, state: FSMContext):
#     if state is None:
#         return
#     await state.finish()
#     await message.reply('Вы прервали получение погоды!', reply_markup=keyboard)
#
#
# async def get_city(message: types.Message):
#     await message.answer('Введите город:', reply_markup=keyboard_cancel)
#     await WeatherStatesGroup.city.set()
#
#
# async def get_weather(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['city'] = message.text.strip().lower()
#     weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={data["city"]}&appid={API}&units=metric')
#     if weather.status_code == 200:
#         weather_img = weather.json()["weather"][0]["icon"]
#         await message.answer_photo(f'https://openweathermap.org/img/wn/{weather_img}@2x.png')
#         await message.answer(f'Сейчас в {data["city"]}: {weather.json()["main"]["temp"]} градусов.', reply_markup=keyboard)
#         await state.finish()
#     else:
#         await message.answer('Что-то пошло не так..')
#         await state.finish()
#
#
# def register_weather_handlers(dp):
#     dp.register_message_handler(cmd_cancel, commands=['отмена'], state='*')
#     dp.register_message_handler(get_city, commands=['погода'])
#     dp.register_message_handler(get_weather, state=WeatherStatesGroup.city)
