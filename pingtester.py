import subprocess
import yaml

class PingTester:
    def __init__(self, hosts_file):
        self.hosts_file = hosts_file
        self.hosts = self.read_hosts()

    def read_hosts(self):
        """Читает список хостов и их описания из YAML файла."""
        with open(self.hosts_file, 'r') as file:
            data = yaml.safe_load(file)
        hosts = []
        if 'hosts' in data:
            for item in data['hosts']:
                if 'host' in item:
                    hosts.append(item['host'])
        return hosts

    def ping_test(self):
        """Пингует все хосты из списка и возвращает результаты."""
        results = {}
        for host in self.hosts:
            response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            results[host] = response.returncode == 0
        return results

    def get_unreachable_hosts(self):
        """Возвращает список недоступных хостов после пинг-теста."""
        results = self.ping_test()
        unreachable_hosts = [host for host, is_reachable in results.items() if not is_reachable]
        return unreachable_hosts
