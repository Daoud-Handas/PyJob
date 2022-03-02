from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


# ***Génère une URL à partir d'un intitulé de poste et la localisation***#

def get_url(position, location):
    template = 'https://fr.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url





# ***Création du modèle de données***#

def get_data_job(card):
    titleSpan = card.h2.span
    soup = BeautifulSoup(response.text, 'html.parser')
    url = ""

    # Comme le salaire n'est pas toujours spécifié, gérer ce cas
    if titleSpan.get("title") is not None:
        job_title = titleSpan.get("title")
    else:
        job_title = "Data Scientist F/H"

    company = card.find("span", "companyName").text.strip()

    job_location = card.find("div", "companyLocation").text

    job_summary = card.find("div", "job-snippet").text.strip()

    post_date = card.find("span", "date").text.strip()

    day = []
    for i in post_date:
        if i.isnumeric():
            day.append(i)
    if day:
        day = "".join(day)
        post_date = datetime.now() - timedelta(days=int(day))
        post_date = post_date.date()
    else:
        post_date = "Today"

    # Comme le salaire n'est pas toujours spécifié, gérer ce cas
    try:
        job_salary = card.find("div", "salary-snippet").text.strip()
    except AttributeError:
        job_salary = None

    # Comme le type de contrat n'est pas toujours spécifié, gérer ce cas
    try:
        job_contract = card.find("span", "jobsearch-JobMetadataHeader-item  icl-u-xs-mt--xs").text.strip()
    except AttributeError:
        job_contract = ""

    # Comme le type de contrat n'est pas toujours spécifié, gérer ce cas
    try:
        tag = card.find_parent('a')
        href = tag.get('href')
        job_url = "https://www.indeed.com" + href
    except AttributeError:
        job_url = ""

    # Le télétravail et le diplome ne sont pas récupérable sur Indeed
    remote = ""
    education_level = ""

    job = {"title": job_title, "company": company, "contract": job_contract, "location": job_location,
           "remote": remote, "education_level": education_level, "description": job_summary,
           "salary": job_salary, "date_published": post_date, "url": job_url}
    return job


def scrap_indeed():
    url = get_url('data scientist', 'Paris')

    # ***Extraire le html du site Indeed***#
    response = requests.get(url)  # response.reason = 'OK' si l'URL est trouvé

    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', 'job_seen_beacon')

    jobs = list()
    for card in cards:
        jobs.append(get_data_job(card))

    return jobs
