from apscheduler.schedulers.background import BackgroundScheduler

from .jobs_getter import job_caller
from ..newsletter import send_newsletter


def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_caller, 'interval', hours=24)
    scheduler.add_job(send_newsletter, 'interval', hours=24)
    scheduler.start()
