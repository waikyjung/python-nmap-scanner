from flask import Flask, render_template, request
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
    display_ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template("ip.html", ip_address=display_ip_address)

if __name__ == "__main__":
    app.run(debug=True)