import json
from collections import OrderedDict

from bs4 import BeautifulSoup
import requests


def print_titles(content):
    for title in content.find_all('strong'):
        print(title.text.strip())


def save_links(content, filename):
    # DS/Algo
    # url = "http://www.geeksforgeeks.org/data-structures/"
    # url = "http://www.geeksforgeeks.org/fundamentals-of-algorithms/"
    # soup = BeautifulSoup(requests.get(url).text)
    # content = soup.find('div', class_="entry-content")

    links = []

    for ul in content.find_all('ul')[1:]:
        topic = OrderedDict()

        for link in ul.find_all('a'):
            if 'geeksquiz' not in link.get('href'):
                topic[link.text.strip()] = link['href'].strip()

        if topic:
            links.append(topic)

    with open(filename, "w") as out:
        json.dump(links, out, indent=4)


def grab_links(urls, filename=None):
    if type(urls) is str:
        urls = [urls]

    links = OrderedDict()

    for url in urls:
        soup = BeautifulSoup(requests.get(url).text)
        content = soup.find('div', id="content")

        topic = OrderedDict()
        for ques in content.find_all("h2", class_="entry-title"):
            link = ques.find("a")
            topic[link.text.strip()] = link['href'].strip()

        # Save topic name too!
        topic_name = url.split('/')[-2].title()
        links[topic_name] = topic

    if not filename:
        print(json.dumps(links, indent=4))
    else:
        with open(filename, "w") as out:
            json.dump(links, out, indent=4)


def unique_links(filename):
    with open(filename) as inp:
        data = json.load(inp, object_pairs_hook=OrderedDict)

    uniq = OrderedDict()
    for title, link in data.items():
        if link not in uniq.values():
            uniq[title] = link

    with open(filename, "w") as out:
        json.dump(uniq, out, indent=4)
