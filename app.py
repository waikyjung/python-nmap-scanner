from flask import Flask, render_template, request
import requests
import nmap
import random
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_number():
    number = random.randint(1, 100)
    return render_template("random.html", random_number=number)

@app.route("/ip_address", methods=["GET"])
def ip_address():
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template("ip.html", ip_address=visitor_ip)

@app.route("/check_ip", methods=["POST"])
def check_ip():
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    #IP Info
    entered_ip = request.form.get("ip")
    response = requests.get(f"https://ipapi.co/{entered_ip}/json/").json()
    
    #Nmap Scan
    '''
    vulnerable_ports = {
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
    ports_to_scan = ','.join(str(port) for port in list(vulnerable_ports.keys()))
    nm = nmap.PortScanner()
    nm.scan(entered_ip, ports_to_scan)

    ports_status = {}
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                state = nm[host][proto][port]['state'].capitalize()
                ports_status[f"{vulnerable_ports[port]} ({port})"] = state
    '''
    
    return render_template("ip.html", 
        ip_address=visitor_ip,
        checked_ip=entered_ip,
        ip_response=response,
        #nmap_response=ports_status
    )

if __name__ == "__main__":
    app.run(debug=True)