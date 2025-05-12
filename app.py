# This project is licensed under the MIT License.
# See the LICENSE file in the root of the repository for details.

from flask import Flask, render_template, request, redirect
from flask_session import Session


app = Flask(__name__)


@app.route("/")
def index():
    # if not logged in render landing page
    if True:
        return render_template("landing.html")

    return render_template("index.html")


@app.route("/landing")
def landing():
    return render_template("landing.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)