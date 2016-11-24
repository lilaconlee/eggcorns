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
    filename = "eggcorn-examples.json"
    entries = {}

    bigSoup = getSoup(BASE_URL)
    lis = bigSoup.select("ul")[0].select("li")
    for li in lis:
        corn = li.text.split(u"»")[1].strip()
        href = li.select("a")[0]['href']
        examples = []

        lilSoup = getSoup(href)
        try:
            foo = lilSoup.select('div[class="occurrences"]')[0].select("li")
            for f in foo:
                example = f.text.split("(")[0]
                if len(example) <= 140:
                    examples.append(example)
            entries[corn] = examples
            print corn
        except IndexError:
            print "no occurrences of " + corn

    with open(filename, 'a') as f:
        json.dump(entries, f)

main()
