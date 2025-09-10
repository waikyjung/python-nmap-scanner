import nmap

# Initialize the scanner
nm = nmap.PortScanner()

# Target and ports
target = "scanme.nmap.org"
ports = "22-443"

print(f"Scanning {target} on ports {ports}...\n")
nm.scan(target, ports)

# Display results
for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        print(f"Protocol: {proto}")
        for port in nm[host][proto]:
            state = nm[host][proto][port]['state']
            print(f"  Port {port}: {state}")
