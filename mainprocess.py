from pingtester import PingTester


# Используем класс PingTester с файлом hosts.yml
tester = PingTester('hosts.yml')

print(tester.get_unreachable_hosts())