# ToDoList app

#### Video Demo: <https://youtu.be/YgfhQaB3N_w>

## Description:
Simple web app for tracking tasks. Made as a final project for **CS50s Introduction to Computer Science**.

## 🚀 Features
- Blazingly fast
- Very simple (even your grandma will get how to use it)
- **Add, Complete or Cancel** task
- **history view**
- Different **priority levels**
- **Cookies support** so you don't have to log in after every refresh
- **Encrypted credentials**: your password is encrypted and secure
- **Responsive design** for desktop and mobile

## 📦 Tech Stack
- **Frontend**: HTML, CSS (vanilla + Bootstrap), JavaScript
- **Backend**: Flask, Flask-session, werkzeug.security
- **Database**: SQLite with help from the CS50 library

## 🧠 Decisions
I wanted to make a todolist app that is very simple and easy to use. I originally planned to make a dashboard tab for charts and other interesting statistics. However, in the end, I decided against that as most of the useful information was already displayed elsewhere and the database was not made to support it. I considered adding dark mode, but I thought that users using that sort of thing are doing so with a browser extension which might interfere with my dark mode.

I might reconsider some of these and add them.

## 📥 Installation (if you want to host the site yourself)
### 1️⃣ Clone the repository
```bash

git clone https://github.com/itsntme1/to-do-list-app.git
cd todolistapp
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask server
```bash
flask run
```

### 5️⃣ Open in your browser
```bash
http://127.0.0.1:5000
```

### 💡 Future Improvements
- User profile settings (change password, email, etc.)
- Category & tag support for tasks
- Email reminders
- Dark mode theme
- History sorting (by creation_date, due_date, etc.)

## 📄 License
MIT License — feel free to use, modify, and distribute.