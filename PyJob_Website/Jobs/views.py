from django.http import HttpResponse
from django.shortcuts import render
from indeed import *

def index(request):
    template = 'https://fr.indeed.com/jobs?q={}&l={}'
    url = template.format('data scientist', 'Paris')
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', 'job_seen_beacon')

    jobs = []
    for card in cards:
        job = get_data_job(card)
        jobs.append(job)
    return render(request, "index.html", context={'jobs' : jobs})
