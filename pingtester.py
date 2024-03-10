import subprocess

class PingTester:
    def __init__(self, hosts_file):
        self.hosts_file = hosts_file
        self.hosts = self.read_hosts()

    def read_hosts(self):
        """Читает список хостов из файла."""
        with open(self.hosts_file, 'r') as file:
            hosts = [line.strip() for line in file if line.strip()]
        return hosts

    def ping_test(self):
        """Пингует все хосты из списка и возвращает результаты."""
        results = {}
        for host in self.hosts:
            response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if response.returncode == 0:
                results[host] = True
            else:
                results[host] = False
        return results

