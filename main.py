from aiogram import Bot, Dispatcher, executor, types
import python_weather



bot = Bot(token= '5411789658:AAHit34wfh2CPMKkTTB_Qbx1riWT6c_twjE')
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + '\n'
    resp_msg += f'Текущая температура: {celsius}°\n'
    resp_msg += f'Состояние погоды: {weather.current.sky_text}'

    if celsius <= 10:
        resp_msg += '\n\nПрохладно! Одевайся теплее!'
    else:
        resp_msg += '\n\nНа улице тепло! '
    await message.answer(resp_msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    #await client.close()

