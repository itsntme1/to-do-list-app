# This project is licensed under the MIT License.
# See the LICENSE file in the root of the repository for details.

from flask import Flask, render_template, request, redirect
from flask_session import Session
from cs50 import SQL


app = Flask(__name__)


db = SQL('sqlite:///todoapp.db')


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


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


@app.route("/register", methods=["GET","POST"])
def register():
    # user is registering
    if request.method == "POST":
        is_validating = True
        username = request.form.get('username')
        password = request.form.get('password')

        # validate form fields
        if not username or not password:
            return render_template("register.html", is_validating=is_validating, username=username, password=password)
        else:
            return redirect('/')
    else:
    # render the form
        return render_template("register.html")


@app.route("/login", methods=["GET","POST"])
def login():
    # user is registering
    if request.method == "POST":
        is_validating = True
        username = request.form.get('username')
        password = request.form.get('password')

        # validate form fields
        if not username or not password:
            return render_template("login.html", is_validating=is_validating, username=username, password=password)
        else:
            return redirect('/')
    else:
    # render the form
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)