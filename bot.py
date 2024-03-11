from telegram_bot_lib import TelegramBot
from config import bot_token, chat_id
from pingtester import PingTester



bot = TelegramBot(chat_id, bot_token)

def ip_test():
    # Используем класс PingTester с файлом hosts.yml
    tester = PingTester('hosts.yml')

    unreachable_hosts = tester.get_unreachable_hosts()
    # Преобразование списка в строку
    mesage_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in  unreachable_hosts])
    print(mesage_bot)
    # Если словарь не пустой то
    if unreachable_hosts:
        bot.send_message(mesage_bot)



ip_test()