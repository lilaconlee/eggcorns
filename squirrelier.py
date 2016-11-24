# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import urllib2
import string

def getSoup(url):
    res = urllib2.urlopen(url)
    html = res.read()
    return BeautifulSoup(html, "lxml")

def main():
    BASE_URL = "http://eggcorns.lascribe.net/browse-eggcorns/"
    filename = "raw-eggcorns.json"
    entries = {}

    bigSoup = getSoup(BASE_URL)
    lis = bigSoup.select("ul")[0].select("li")
    for li in lis:
        eggcorn = li.text.split(u"»")
        egg = eggcorn[0].strip()
        corn = eggcorn[1].strip()
        entries[egg] = corn;

    with open(filename, 'a') as f:
        json.dump(entries, f)

main()
