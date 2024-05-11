import requests
from bs4 import BeautifulSoup
import sys
import time


def parse(arg1, arg2):
    url = f'https://finance.yahoo.com/quote/{arg1}/financials?p={arg1}'
    resp = requests.get(url, headers={'User-Agent': 'Custom'})
    bs = BeautifulSoup(resp.text, 'html.parser')
    title = bs.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise Exception('Wrong ticker')
    tags = bs.find_all(attrs={'data-test': 'fin-row'})
    breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if arg2 not in breakdowns:
        raise Exception('Not found breakdown')
    time.sleep(5)
    print(tuple(t.get_text() for t in tags[breakdowns.index(arg2)].find_all('span')))
    return (arg1, arg2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Wrong Number of ARGs!")
    else:
        parse(sys.argv[1], sys.argv[2])