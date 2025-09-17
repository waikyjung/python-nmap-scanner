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

@app.route("/ip_address", methods=["GET"])
def ip_address():
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template("ip.html", ip_address=visitor_ip)

@app.route("/check_ip", methods=["POST"])
def check_ip():
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    entered_ip = request.form.get("ip")
    response = requests.get(f"https://ipapi.co/{entered_ip}/json/").json()
    if response.get("vpn") or response.get("proxy"):
        is_vpn_or_proxy = "Yes"
    else:
        is_vpn_or_proxy = "No"

    return render_template("ip.html", 
        ip_address=visitor_ip,
        checked_ip=entered_ip,
        vpn_status=is_vpn_or_proxy
    )

if __name__ == "__main__":
    app.run(debug=True)