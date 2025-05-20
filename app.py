# This project is licensed under the MIT License.
# See the LICENSE file in the root of the repository for details.

from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)


db = SQL('sqlite:///todoapp.db')


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    # user is submitting a new task
    if request.method == 'POST':
        content = request.form.get('content')
        date = request.form.get('date')
        priority = request.form.get('priority')

        # validation
        if not content:
            return render_template("index.html")
        
        # insert a task into the tasks table
        db.execute("INSERT INTO tasks (user_id, content, due_date, priority) VALUES(?, ?, ?, ?)",
                   session['user_id'], content, date, priority)

        return render_template("index.html")

    else:
        # if not logged in render landing page
        if not session.get('user_id'):
            return render_template("landing.html")

        return render_template("index.html")


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
        username = request.form.get('username')
        password = request.form.get('password')

        # validate form fields
        if not username or not password:
            print('there')
            return render_template("register.html", is_validating=True, isUnique=False, username=username, password=password)
        else:
            # try if the username is unique
            try:
                # insert user into the database
                db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                        username, generate_password_hash(password))
                # remember that the user is logged in
                session['user_id'] = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]
            except:
                return render_template("register.html", is_validating=True, isUnique=False, username=username, password=password)
            
            return redirect('/')
    else:
    # render the form
        return render_template("register.html")


@app.route("/login", methods=["GET","POST"])
def login():
    # user is logging in
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # forget any user_id
        session.clear()

        # validate form fields
        if not username or not password:
            return render_template("login.html", is_validating=True, username=username, password=password)
        
        # get a record of the apropriate username
        record = db.execute("SELECT * FROM users WHERE username = ?", username)

        # check username and password
        if len(record) != 1 or not check_password_hash(record[0]["password_hash"], password):
            return render_template("login.html", is_validating=True, isWrong=True, username=username, password=password)
        
        # remember that the user is logged in
        session['user_id'] = record[0]['id']

        return redirect('/')
    else:
    # render the form
        return render_template("login.html")
    

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
