#!/usr/bin/env python2.7

import os
import sys
import json

from collections import OrderedDict

import requests

import glean

ROOT = "Topics"
ROOT_HTML = "HTML"


def mkdir(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)


def download(urls, folder):
    mkdir(folder)
    cleaned_html = []

    for url in urls:
        file = os.path.join(folder, url.split('/')[-2] + ".html")

        if os.path.isfile(file):
            with open(file) as inp:
                cleaned_html.append(inp.read())
            continue

        print(file)
        r = requests.get(url)
        cleaned_html.append(glean.clean(r.content))

        with open(file, 'wb') as out:
            out.write(glean.clean(r.content))

    cleaned_file = os.path.join(
        ROOT_HTML,
        folder.split('/')[-1] + ".html"
    )

    with open(cleaned_file, 'wb') as out:
        out.write("\n".join(cleaned_html))


def download_from_json_with_topic_keys(ds):

    # Only download these topics
    # some_topics = [
    #     'Graphs',
    #     'Binary Trees',
    # ]

    for topic in ds.keys():
        # for topic in some_topics:
        if topic in ['Advanced Data Structures']:
            urls = []
            for sub_topic in ds[topic]:
                urls += ds[topic][sub_topic].values()
            download(urls, os.path.join(ROOT, topic))
        else:
            download(ds[topic].values(), os.path.join(ROOT, topic))


def download_from_json(ds, tag_name):
    download(ds.values(), os.path.join(ROOT, tag_name))


if __name__ == '__main__':
    TAG = sys.argv[1]
    fname = "JSON/%s.json" % TAG

    with open(fname) as inp:
        ds = json.load(inp, object_pairs_hook=OrderedDict)

    # download_from_json_with_topic_keys(ds)
    download_from_json(ds, TAG)
