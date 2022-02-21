from datetime import date, datetime

import requests
import xmltodict as xmltodict

from ..models import Job


def scrap_monster_jobs():
    today = date.today()

    query_search = {'q': 'python'}  # here goes the variable

    r = requests.get('https://rss.jobsearch.monster.com/rssquery.ashx?q=python', params=query_search, verify=False)

    if r.status_code == 200:
        o_dict = xmltodict.parse(r.content)

        jobs = [{
            'title': job['title'],
            'description': job['description'],
            'date_published': datetime.strptime(job['pubDate'], '%a, %d %b %Y %H:%M:%S %Z'),
            'url': job['link'],
        }
            for job in o_dict['rss']['channel']['item']]

        # create new instance
        for job in jobs:
            new_job = Job(**job)
            new_job.save()
        # save to database

