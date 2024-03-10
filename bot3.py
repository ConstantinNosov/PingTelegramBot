import asyncio
from aiogram import Bot, Dispatcher
from pingtester import PingTester
from config import bot_token, chat_id

async def send_message_forever(bot):
    while True:
        tester = PingTester('hosts.yml')
        unreachable_hosts = tester.get_unreachable_hosts()

        if unreachable_hosts:
            message_text = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in unreachable_hosts])
            try:
                await bot.send_message(chat_id, message_text)
                print("Сообщение отправлено")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        else:
            print("Все хосты доступны.")
        
        await asyncio.sleep(300)  # Пауза в 5 минут

async def main():
    bot = Bot(token=bot_token)
    dp = Dispatcher(bot)

    # Запускаем фоновую задачу отправки сообщений
    task = asyncio.create_task(send_message_forever(bot))

    # Здесь можно добавить другие асинхронные задачи, если это необходимо

    # Ожидаем завершения задачи (в данном случае это не произойдет, так как задача бесконечна)
    await task

if __name__ == '__main__':
    asyncio.run(main())
