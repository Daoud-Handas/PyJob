from apscheduler.schedulers.background import BackgroundScheduler

from .jobs_getter import job_caller


def schedule():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(job_caller(), 'interval', hours=24)
    scheduler.start()
