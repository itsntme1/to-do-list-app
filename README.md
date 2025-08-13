# ToDoList app

#### Video Demo: <https://youtu.be/YgfhQaB3N_w>

## Description:
Simple web app for tracking tasks. Made as a final project for CS50.

## 🚀 Features
- blazingly fast
- very simple (even your grandma will get how to use it)
- **Add, Complete or Cancel** task
- **history view**
- Different **priority levels**
- **Cookies support** so you don't have to login after every refresh
- **Encrypted credentials**: your password is encrypted and secure
- **Responsive design** for desktop and mobile

## 📦 Tech Stack
- **Frontend**: HTML, CSS (vanilla + Bootstrap), JavaScript
- **Backedn**: Flask, Flask-session, werkzeug.security
- **Database**: SQLite with help from the CS50 library

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

## 📄 License
MIT License — feel free to use, modify, and distribute.