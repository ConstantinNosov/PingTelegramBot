import logging
from telegram import Bot
from threading import Thread
import time
import schedule

# Замените 'YOUR_TOKEN_HERE' на токен вашего бота
TOKEN = 'YOUR_TOKEN_HERE'
# Замените 'CHAT_ID_HERE' на ID чата, куда бот будет отправлять сообщения
CHAT_ID = 'CHAT_ID_HERE'

bot = Bot(token=TOKEN)

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция, которая проверяет условие и отправляет сообщение
def check_and_send_message():
    ping_fail = None  # Пример условия, здесь должна быть ваша логика проверки
    if ping_fail is None:
        bot.send_message(chat_id=CHAT_ID, text="ping_fail is None")

# Функция для запуска планировщика
def run_scheduler():
    schedule.every(10).seconds.do(check_and_send_message)  # Проверка каждые 10 секунд

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Запускаем планировщик в отдельном потоке
    thread = Thread(target=run_scheduler)
    thread.start()

    # В этом месте могут быть другие задачи, если они есть
