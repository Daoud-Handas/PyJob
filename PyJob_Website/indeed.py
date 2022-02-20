import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


# ***Génère une URL à partir d'un intitulé de poste et la localisation***#

def get_url(position, location):
    template = 'https://fr.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url


url = get_url('data scientist', 'Paris')

# ***Extraire le html du site Indeed***#

response = requests.get(url)  # response.reason = 'OK' si l'URL est trouvé

soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('div', 'job_seen_beacon')


# ***Création du modèle de données***#

def get_data_job(card):
    # aTag = card.a
    titleSpan = card.h2.span

    job_title = titleSpan.get("title")

    # job_url = "https://www.indeed.com" + aTag.get("href")

    company = card.find("span", "companyName").text.strip()

    job_location = card.find("div", "companyLocation").text

    job_summary = card.find("div", "job-snippet").text.strip()

    post_date = card.find("span", "date").text.strip()

    today = datetime.today().strftime("%d-%m-%Y")

    # Comme le salaire n'est pas toujours spécifié, gérer ce cas
    try:
        job_salary = card.find("div", "salary-snippet").text.strip()
    except AttributeError:
        job_salary = ""

    # Comme le type de contrat n'est pas toujours spécifié, gérer ce cas
    try:
        job_contract = card.find("span", "jobsearch-JobMetadataHeader-item  icl-u-xs-mt--xs").text.strip()
    except AttributeError:
        job_contract = ""

    # Comme le type de contrat n'est pas toujours spécifié, gérer ce cas
    try:
        job_url = card.find("span", "jobsearch-JobMetadataHeader-item  icl-u-xs-mt--xs").text.strip()
    except AttributeError:
        job_url = ""


    # Le télétravail et le diplome ne sont pas récupérable sur Indeed
    remote = ""
    education_level = ""

    job = {"title": job_title, "company": company, "contract": job_contract, "location": job_location,
           "remote": remote, "education_level": education_level, "description": job_summary,
           "salary": job_salary, "date": post_date, "url": job_url}
    return job


