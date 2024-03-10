from pingtester import PingTester
import telegram
import asyncio
from config import bot_token, chat_id

async def send_message_forever():
    bot = telegram.Bot(token=bot_token)
    while True:
        tester = PingTester('hosts.yml')
        unreachable_hosts = tester.get_unreachable_hosts()

        if unreachable_hosts:
            message_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in unreachable_hosts])

            try:
                await bot.send_message(chat_id=chat_id, text=message_bot)  # Асинхронный вызов
                print("Сообщение отправлено")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        else:
            print("Все хосты доступны.")
        
        # Пауза в 5 минут перед следующей проверкой
        await asyncio.sleep(10)

# Запускаем асинхронную функцию в бесконечном цикле
asyncio.run(send_message_forever())
