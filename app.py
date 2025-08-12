# This project is licensed under the MIT License.
# See the LICENSE file in the root of the repository for details.

from flask import Flask, render_template, request, redirect, session, jsonify
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

from flask_filters import *
from helpers import *


app = Flask(__name__)


db = SQL('sqlite:///todoapp.db')


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# register filters
app.jinja_env.filters['format_none'] = format_none
app.jinja_env.filters['format_date'] = format_date
app.jinja_env.filters['format_priority'] = format_priority
app.jinja_env.filters['priority_text_bg_color'] = priority_text_bg_color
app.jinja_env.filters['priority_table_color'] = priority_table_color
app.jinja_env.filters['format_status_table'] = format_status_table


@app.route("/", methods=['GET', 'POST'])
def index():
    # user is submitting a new task
    if request.method == 'POST':
        content = request.form.get('content')
        date = request.form.get('date')
        priority = request.form.get('priority')

        # validation
        if not content or len(content) > 60:
            return redirect('/')
        
        # insert a task into the tasks table
        db.execute("INSERT INTO tasks (user_id, content, due_date, priority) VALUES(?, ?, ?, ?)",
                   session['user_id'], content, date, priority)
        
        return redirect('/')

    # if logged in
    elif session.get('user_id'):
        upcoming_tasks = db.execute("SELECT id, content, due_date, priority FROM tasks WHERE user_id = ? AND status == 'pending' ORDER BY due_date == '', due_date ASC", session["user_id"])

        important_tasks = db.execute("SELECT id, content, priority FROM tasks WHERE user_id = ? AND priority != '' AND status == 'pending' ORDER BY priority DESC", session["user_id"])
        
        return render_template("index.html", upcoming_tasks=upcoming_tasks, important_tasks=important_tasks)

    else:
        return render_template("landing.html")


@app.route("/history")
@login_required
def history():
    records = db.execute("SELECT content, creation_date, due_date, priority, status FROM tasks WHERE user_id = ? ORDER BY creation_date DESC", session["user_id"])

    return render_template("history.html", records=records)


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


@app.route('/complete_task', methods=['POST'])
def complete_task():
    data = request.get_json()
    task_id = data.get('id')

    print('here')

    if task_id:
        db.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", task_id)

        return jsonify({'success': True})

    return jsonify({'success': False, 'error': 'Task not found'}), 404


@app.route('/cancel_task', methods=['POST'])
def cancel_task():
    data = request.get_json()
    task_id = data.get('id')

    print('here')

    if task_id:
        db.execute("UPDATE tasks SET status = 'canceled' WHERE id = ?", task_id)

        return jsonify({'success': True})

    return jsonify({'success': False, 'error': 'Task not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)
