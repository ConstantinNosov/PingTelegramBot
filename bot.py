from bot_lib import TelegramBot
from config import bot_token, chat_id
from pingtester_lib import PingTester
import time


bot = TelegramBot(chat_id, bot_token)

def ip_test():
    tester = PingTester('hosts.yml')
    unreachable_hosts = tester.get_unreachable_hosts()
    message_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in  unreachable_hosts])
    # Если словарь не пустой то
    if unreachable_hosts:
        bot.send_message(message_bot)

while True:
    ip_test()
    time.sleep(1800)