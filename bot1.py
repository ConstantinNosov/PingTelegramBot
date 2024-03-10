from pingtester import PingTester
import telebot
import asyncio
from config import bot_token, chat_id

async def send_message_forever():
    bot = telebot.TeleBot(bot_token)
    
    while True:
        tester = PingTester('hosts.yml')
        unreachable_hosts = tester.get_unreachable_hosts()

        if unreachable_hosts:
            message_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in unreachable_hosts])
            
            try:
                # telebot не поддерживает асинхронный вызов напрямую
                # поэтому используем run_until_complete для совместимости
                loop = asyncio.get_event_loop()
                loop.run_until_complete(loop.run_in_executor(None, bot.send_message, chat_id, message_bot))
                print("Сообщение отправлено")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        else:
            print("Все хосты доступны.")
        
        # Пауза в 5 минут перед следующей проверкой
        await asyncio.sleep(10)

# Так как telebot не предоставляет асинхронный интерфейс,
# вам может потребоваться адаптировать код для полной асинхронной работы,
# например, использовать асинхронную оболочку или менеджер задач.

# Запускаем асинхронную функцию в бесконечном цикле
asyncio.run(send_message_forever())
