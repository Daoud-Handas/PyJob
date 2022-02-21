from apscheduler.schedulers.background import BackgroundScheduler

from . import scrap_monster


def schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrap_monster.scrap_monster_jobs, 'interval', seconds=5)
    scheduler.start()
