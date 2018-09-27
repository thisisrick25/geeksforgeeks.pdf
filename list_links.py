#!/usr/bin/env python3.6

"""
List all links on all pages of a geeks for geeks tag.

Usage: list_links samsung

By default, a JSON is generated, which can be edited by hand.
"""

import sys
import json

from collections import OrderedDict

import requests
import pyquery

from bs4 import BeautifulSoup

TAG = sys.argv[1]
TAG_URL = f"https://www.geeksforgeeks.org/tag/{TAG}"

ROOT_JSON = "JSON"
FNAME = ROOT_JSON + f"{TAG}.json"


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


def fetch_post_links(urls, filename=None, combined=False):
    if type(urls) is str:
        urls = [urls]

    links = OrderedDict()

    for url in urls:
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        content = soup.find('div', id="content")

        topic = OrderedDict()
        for ques in content.find_all("h2", class_="entry-title"):
            link = ques.find("a")
            topic[link.text.strip()] = link['href'].strip()

        if combined:
            links.update(topic)
        else:
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


def list_pages(root_url):

    links = []

    pq = pyquery.PyQuery(url=root_url)
    if pq('a.last'):
        last_url = pq('a.last')[0].get('href')
        last_url = [p for p in last_url.split("/") if p]
        num_pages = int(last_url[-1])

    for page in range(1, num_pages + 1):
        links.append(TAG_URL + f"/page/{page}/")

    return links


if __name__ == '__main__':
    fetch_post_links(list_pages(TAG_URL), FNAME, combined=True)
    unique_links(FNAME)
