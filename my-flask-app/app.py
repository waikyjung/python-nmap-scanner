from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_number():
    number = random.randint(1, 100)
    return render_template("random.html", random_number=number)


if __name__ == "__main__":
    app.run(debug=True)