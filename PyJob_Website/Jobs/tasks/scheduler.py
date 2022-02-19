from apscheduler.schedulers.background import BackgroundScheduler

from . import status


def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(status.printo, 'interval', seconds=5)
    scheduler.start()
