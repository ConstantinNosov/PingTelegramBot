from pingtester import PingTester
import time

while True:
    # Используем класс PingTester с файлом hosts.txt
    tester = PingTester('hosts.txt')
    dictionary_ping = tester.ping_test()

    # Найти и распечатать все IP-адреса с значением False
    ping_fail=None
    for ping_fail, status in dictionary_ping.items():
        if not status:
            print(f"{ping_fail} не в сети")
    time.sleep(2)