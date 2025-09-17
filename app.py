from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_number():
    number = random.randint(1, 100)
    return render_template("random.html", random_number=number)

@app.route("/ip_address")
def ip_address():
    visitor_ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    response = requests.get(f"https://ipapi.co/{visitor_ip_address}/json/").json()
    if response.get("vpn") or response.get("proxy"):
        is_vpn_or_proxy = True
    else:
        is_vpn_or_proxy = False

    return render_template("ip.html", 
        ip_address=visitor_ip_address,
        vpn_status=is_vpn_or_proxy
    )

if __name__ == "__main__":
    app.run(debug=True)