from flask import Flask

from background import scheduler


class Config:
    APP_SECRET = 'Hidden Leaf'


def create_app():
    f = Flask(__name__)
    f.config.from_object(Config)
    scheduler.init_app(f)
    scheduler.start()

    @f.route('/')
    def index():
        return 'Hello.', 200

    return f

