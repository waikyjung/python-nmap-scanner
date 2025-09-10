import re
import nmap
from colorama import Fore, Style, init

# Initialize
init(autoreset=True)
nm = nmap.PortScanner()

# Target and ports
def is_valid_ipv4(ip):
    pattern = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}' \
              r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
    return re.match(pattern, ip) is not None

high_risk_ports = {
  21: 'FTP',
  22: 'SSH',
  23: 'Telnet',
  25: 'SMTP',
  53: 'DNS',
  80: 'HTTP',
  110: 'POP3',
  139: 'SMB',
  143: 'IMAP',
  445: 'SMB',
  3389: 'RDP',
  5900: 'VNC'
}
ports_to_scan = ','.join(str(port) for port in list(high_risk_ports.keys()))
#target = "45.33.32.156"
target = input("Enter a IPv4 address to scan: ")

if is_valid_ipv4(target) == False:
    print(f"\"{target}\" is not a valid IPv4 address.")
else:
    print(f"Scanning \"{target}\" for vulnerable ports...\n")
    nm.scan(target, ports_to_scan)

    # Display results
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state().capitalize()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto.upper()}")
            for port in nm[host][proto]:
                state = nm[host][proto][port]['state'].capitalize()
                print(f"  Port {port} ({high_risk_ports[port]}): ", end="")
                if state == "Open":
                    print(f"{Fore.RED}{state}{Style.RESET_ALL}")
                elif state == "Closed":
                    print(f"{Fore.GREEN}{state}{Style.RESET_ALL}")
