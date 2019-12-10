from flask import Flask

from background import scheduler


def create_app():
    f = Flask(__name__)
    scheduler.init_app(f)
    scheduler.start()
    return f

