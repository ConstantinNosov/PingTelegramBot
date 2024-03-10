from pingtester import PingTester

def send_mesage():
    # Используем класс PingTester с файлом hosts.yml
    tester = PingTester('hosts.yml')

    unreachable_hosts = tester.get_unreachable_hosts()

    # Если словарь не пустой то
    if unreachable_hosts:
        print("Команда боту написать сообщение")
        # Преобразование списка в строку
        mesage_bot = ', '.join([f"{item['description']}: {item['host']} нет ping" for item in  unreachable_hosts])
        print(mesage_bot)


send_mesage()