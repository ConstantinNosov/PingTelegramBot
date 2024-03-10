from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
from pingtester import PingTester
from config import bot_token, chat_id

# Создаем экземпляр бота
bot = Bot(token=bot_token)
# Создаем диспетчер
dp = Dispatcher(bot)

async def send_message_forever():
    while True:
        tester = PingTester('hosts.yml')
        unreachable_hosts = tester.get_unreachable_hosts()

        if unreachable_hosts:
            message_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in unreachable_hosts])

            try:
                await bot.send_message(chat_id, message_bot)
                print("Сообщение отправлено")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        else:
            print("Все хосты доступны.")

        # Пауза в 5 минут перед следующей проверкой
        await asyncio.sleep(300)  # Изменил на 300 секунд, что соответствует 5 минутам

if __name__ == "__main__":
    # Запускаем фоновую задачу
    dp.loop.create_task(send_message_forever())
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
