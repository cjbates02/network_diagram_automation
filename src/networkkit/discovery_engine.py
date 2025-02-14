# nmap -sn 10.0.97.0/24
import subprocess
import re

class DiscoveryEngine:
    def __init__(self, network):
        self.network = network
        self.new_endpoints = set()
        
    
    def discover_endpoints(self):
        try:
            output = subprocess.check_output(['nmap', '-sn', self.network], text=True)
            ip_addresses = self.parse_ip_addresses(output)
            print(ip_addresses)
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute 'nmap -sn' scan on {network}. Exit code: {e.returncode}")
    
    
    def parse_ip_addresses(self, output):
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        matches = re.findall(ip_pattern, output)
        return matches


if __name__ == '__main__':
    discovery_engine = DiscoveryEngine('10.0.97.0/24')
    discovery_engine.discover_endpoints()