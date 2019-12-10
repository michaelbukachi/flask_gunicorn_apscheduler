import logging

from gevent import monkey

monkey.patch_all()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
else:
    gunicorn_logger = logging.getLogger('gunicorn.debug')
    app.logger.addHandler(gunicorn_logger)