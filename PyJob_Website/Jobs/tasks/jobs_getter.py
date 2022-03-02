from .welcome_to_jungle import scrap_welcome_to_the_jungle
from .scrap_monster import scrap_monster_jobs
from .indeed import scrap_indeed
from ..models import Job, Email


def job_exist(url):
    database_job = Job.objects.filter(url=url)
    if len(database_job) == 0:
        return False
    else:
        return True


def verify(jobs):
    return [job for job in jobs if not job_exist(job["url"])]


def save_jobs(jobs):
    for job in jobs:
        new_job = Job(**job)
        new_job.save()


def job_caller():
    jobs = list()
    jobs += scrap_monster_jobs()
    print("scrap monster done !")
    jobs += scrap_welcome_to_the_jungle()
    print("scrap welcome to the jungle done !")
    jobs += scrap_indeed()
    print("scrap indeed done !")

    jobs = verify(jobs)
    print("job verifiés")
    save_jobs(jobs)
    print("end !")
