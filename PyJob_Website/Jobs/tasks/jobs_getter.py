from .welcome_to_jungle import scrap_welcome_to_the_jungle
from .scrap_monster import scrap_monster_jobs
from .indeed import scrap_indeed
from ..models import Job


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
        print(f"job ajouté : {job['url']}")


def job_caller():
    jobs = list()
    jobs += scrap_welcome_to_the_jungle()
    jobs += scrap_monster_jobs()
    jobs += scrap_indeed()

    jobs = verify(jobs)
    print("job verifiés")
    save_jobs(jobs)
    print("end !")
