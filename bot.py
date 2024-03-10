from pingtester import PingTester
import telegram
import asyncio
from config import bot_token, chat_id 

async def send_message():
    
    bot = telegram.Bot(token=bot_token)

    # Используем класс PingTester с файлом hosts.yml
    tester = PingTester('hosts.yml')
    unreachable_hosts = tester.get_unreachable_hosts()

    # Если словарь не пустой, то
    if unreachable_hosts:
        message_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in unreachable_hosts])
        
        try:
            await bot.send_message(chat_id=chat_id, text=message_bot)  # Используем await для асинхронного вызова
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
    else:
        print("Все хосты доступны.")

# Запускаем асинхронную функцию
asyncio.run(send_message())
