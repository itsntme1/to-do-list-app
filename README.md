# ToDoList app

#### Video Demo: <https://youtu.be/YgfhQaB3N_w>

## Description:
Simple web app for tracking tasks. Made as a final project for **CS50's Introduction to Computer Science**.

## 🚀 Features
- Blazingly fast
- Very simple (even your grandma will get how to use it)
- **Add, Complete or Cancel** task
- **History view**
- Different **priority levels**
- **Cookies support** so you don't have to log in after every refresh
- **Encrypted credentials**: your password is encrypted and secure
- **Responsive design** for desktop and mobile

## 📦 Tech Stack
- **Frontend**: HTML, CSS (vanilla + Bootstrap), JavaScript
- **Backend**: Flask, Flask-session, werkzeug.security
- **Database**: SQLite with help from the CS50 library

## 🧠 Decisions
I wanted to make a todolist app that is very simple and easy to use.

I originally planned to make a dashboard tab for charts and other interesting statistics. However, in the end, I decided against that as most of the useful information was already displayed elsewhere and the database was not made to support it.

I considered adding dark mode, but many users already use browser extensions for that, which could conflict with the implementation.

I might reconsider some of these and add them.


## 🗂 File structure
```bash
.
├── app.py
├── flask_filters.py
├── flask_session
├── helpers.py
├── LICENSE
├── README.md
├── requirements.txt
├── static
│   ├── favicon.svg
│   └── style.css
├── templates
│   ├── history.html
│   ├── index.html
│   ├── landing.html
│   ├── layout.html
│   ├── login.html
│   └── register.html
└── todoapp.db
```
- app.py: the core server-side logic
- flask_filters: mainly used for custom flask filters to improve readability of the templates
- flask_session: contains session data
- helpers.py: used for `login_required` functionality and some abandoned graph code using matplotlib
- requirements.txt: used for installing dependencies (more in the Installation section)
- static/style.css: custom styles for things I couldn't do with Bootstrap
- templates: templates for each of the pages
- todoapp.db: the SQLite database (contains testing data)
- README.md: the file you are reading right now


## 📥 Installation (if you want to host the site yourself)
### 1️⃣ Clone the repository
```bash

git clone https://github.com/itsntme1/to-do-list-app.git
cd to-do-list-app
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

## 🤝 How to Contribute
Contributions are welcome! Whether it’s fixing bugs, adding new features, or improving documentation, you can help make this app better.

### 1️⃣ Fork the Repository
Click the Fork button on GitHub to create your own copy of the project.

### 2️⃣ Clone Your Fork
```bash
git clone https://github.com/<your-username>/to-do-list-app.git
cd todolistapp
```

### 3️⃣ Create a New Branch
Create a separate branch for your work. Give it a descriptive name:
```bash
git checkout -b feature/add-dark-mode
```

### 4️⃣ Make Changes
- Implement your changes locally.
- Ensure your code is clean and follows existing style conventions.
- Update README.md or other documentation if needed.

### 5️⃣ Commit Your Changes
Write clear, concise commit messages:

```bash
git add .
git commit -m "Add dark mode toggle"
```

### 6️⃣ Push to Your Fork
```bash
git push origin feature/add-dark-mode
```

### 7️⃣ Open a Pull Request
- Go to the original repository on GitHub.
- Click Compare & pull request.
- Describe your changes, why they’re needed, and submit the PR.

## 💡 Future Improvements
- User profile settings (change password, email, etc.)
- Category & tag support for tasks
- Email reminders
- Dark mode theme
- History sorting (by creation_date, due_date, etc.)

## 📄 License
MIT License — feel free to use, modify, and distribute.