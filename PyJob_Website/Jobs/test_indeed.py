from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# ***Génère une URL à partir d'un intitulé de poste et la localisation***#
from PyJob.PyJob_Website.Jobs.indeed import get_data_job


def get_url(position, location):
    template = 'https://fr.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url


url = get_url('data scientist', 'Paris')

# ***Extraire le html du site Indeed***#

response = requests.get(url)  # response.reason = 'OK' si l'URL est trouvé

# ***Création du modèle de données***#


template = 'https://fr.indeed.com/jobs?q={}&l={}'
url = template.format('data scientist', 'Paris')
soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find('div', 'job_seen_beacon')
tag = cards.find_parent('a')
href = tag.get('href')

print(href)

