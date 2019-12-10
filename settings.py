import multiprocessing

from gevent import monkey

monkey.patch_all()

bind = '0.0.0.0:5000'
worker_class = 'gevent'
workers = 1
threads = (2 * multiprocessing.cpu_count()) + 1
loglevel = 'debug'
keepalive = 10
timeout = 30


