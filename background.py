import datetime

from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.gevent import GeventScheduler
from flask_apscheduler import APScheduler


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 20
}

sched = GeventScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults,)

scheduler = APScheduler(sched)


@scheduler.task('interval', id='do_something_job',  seconds=10, next_run_time=datetime.datetime.now())
def do_something_job():
    print('I\'m doing something')

