from datetime import datetime

import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup


def get_jobs_list(query_soup):
    # getting the 'ol' (list) HTML element
    ol = query_soup.find("ol")

    # getting all the {url, date}
    list_job = [{"url": get_a(d), "date_published": get_date(d)} for d in ol.contents if d.name == 'li']

    return list_job


def get_a(li):
    return "https://www.welcometothejungle.com" + li.find(lambda tag: tag.name == 'a').get("href")


def get_date(li):
    return li.find(lambda tag: tag.name == "time").get("datetime")


# job argument is a dict : {url, date_published}
def scrap_job_data(job):
    job_soup = get_normal_HTML(job["url"])

    # get job title
    title = job_soup.find("h1").string
    # get the "ul" list with the attribute : data-testid="job-header-metas"
    ul = job_soup.find(lambda tag: tag.name == "ul" and tag.get("data-testid") == "job-header-metas")
    # get the "div" where is the job description
    description_div = job_soup.find(
        lambda tag: tag.name == "h2" and (tag.string == "Job description" or tag.string == "Descriptif du poste"))

    if description_div is not None and description_div.nextSibling is not None:
        description = get_job_description(description_div.nextSibling)
    else:
        # for none english or french
        first_h2 = job_soup.find("h2")
        description = first_h2.parent.parent.text

    # extracting datas from tag object
    job_data = get_job_metas(ul.contents)
    job_data["title"] = title
    job_data["description"] = description
    # job_data["date_published"] = job["date_published"]
    job_data.update(job)
    job_data["company"] = get_company(job["url"])

    return job_data


def get_job_metas(list_li):
    data = {}
    for li in list_li:
        name = li.contents[0].contents[0].get("name")
        value = li.contents[1].contents[0].string
        if name == "clock":
            name = "date_start"
        if name not in data:
            data[name] = value

    return data


def get_job_description(description_div):
    description = ""
    for child in description_div.children:
        if child.name == "p":
            description += child.text
        else:
            for li in child.children:
                description += " - " + li.text
        description += '\n'
    return description


def get_company(job_url):
    elements = job_url.split('/')
    company_index = elements.index("companies") + 1

    return elements[company_index]


def get_normal_HTML(url):
    response = requests.get(url)
    htmltext = response.text
    return BeautifulSoup(htmltext, 'html.parser')


# with js loaded
def get_updated_HTML(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout=50)
    soup = BeautifulSoup(response.html.html, "html.parser")
    ol = soup.find("ol")
    i = 0

    while ol is None:
        response.session.close()
        session = HTMLSession()
        response = session.get(url)
        response.html.render(timeout=20)
        soup = BeautifulSoup(response.html.html, "html.parser")
        ol = soup.find("ol")
        i = i + 1

    # TODO log or delete
    # print(f"retry number {i}, total time : {datetime.now() - now}")

    response.session.close()

    return soup


def scrap_welcome_to_the_jungle():
    query_url = "https://www.welcometothejungle.com/fr/jobs?query=python"
    soup = get_updated_HTML(query_url)
    jobs_url = get_jobs_list(soup)
    jobs_dicts = list()
    for job in jobs_url:
        jobs_dicts.append(scrap_job_data(job))

    return jobs_dicts
