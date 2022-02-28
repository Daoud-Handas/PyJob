from django.http import HttpResponse
from django.shortcuts import render
from .indeed import *
from .models import Job


def index(request):
    template = 'https://fr.indeed.com/jobs?q={}&l={}'
    url = template.format('data scientist', 'Paris')
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', 'job_seen_beacon')

    jobs = []
    for card in cards:
        job = get_data_job(card)
        o = Job(**job)
        o.save()
        jobs.append(Job(**job))

    #jobs = Job.objects.all()[:15]

    return render(request, "index.html", context={'jobs': jobs})