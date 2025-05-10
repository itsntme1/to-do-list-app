# This project is licensed under the MIT License.
# See the LICENSE file in the root of the repository for details.

from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/history")
def history():
    return render_template("history.html")


if __name__ == "__main__":
    app.run(debug=True)