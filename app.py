from flask import Flask, render_template
import os

app = Flask(__name__)

ENVIRONMENT = os.getenv("APP_ENV", "Development")

@app.route("/")
def home():
    return render_template("index.html", env=ENVIRONMENT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
