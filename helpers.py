import matplotlib.pyplot as plt
from flask import session, redirect
from functools import wraps


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            return redirect('/login')
        
        return func(*args, **kwargs)

    return wrapper


def plot_pie(data: list[int], labels: list[str]):
    plt.pie(data, labels=labels)

    plt.show()

//starship prompt test 2