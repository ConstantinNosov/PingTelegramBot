import subprocess
import yaml

class PingTester:
    def __init__(self, hosts_file):
        self.hosts_file = hosts_file
        # Сохранение полных данных о хостах
        self.hosts = self.read_hosts()

    def read_hosts(self):
        """Читает список хостов и их описания из YAML файла."""
        with open(self.hosts_file, 'r') as file:
            data = yaml.safe_load(file)
        #Сохранение хостов с описаниями
        hosts = []
        if 'hosts' in data:
            for item in data['hosts']:
                if 'host' in item and 'description' in item:
                    # Сохранение словаря для каждого хоста
                    hosts.append({'host': item['host'], 'description': item['description']})
        return hosts

    def ping_test(self):
        """Пингует все хосты из списка и возвращает результаты с описаниями."""
        results = {}
        for host_info in self.hosts:
            host = host_info['host']
            response = subprocess.run(['ping', '-c', '3', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Включение описания в результаты
            results[host] = {'reachable': response.returncode == 0, 'description': host_info['description']}
        return results

    def get_unreachable_hosts(self):
        """Возвращает список недоступных хостов с их описаниями после пинг-теста."""
        results = self.ping_test()
        # Включение описаний в вывод
        unreachable_hosts = [{ 'host': host, 'description': info['description']} 
                             for host, info in results.items() if not info['reachable']]
        return unreachable_hosts


