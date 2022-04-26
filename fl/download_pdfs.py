import datetime
import random
import time

import bs4
import requests


URL = 'http://www.dc.state.fl.us/pub/jails/index.html'
BASE = 'http://www.dc.state.fl.us/pub/jails/'


def parse_dt(s: str) -> datetime.datetime:
    s = s.replace('report', '').strip()
    return datetime.datetime.strptime(s, '%B %Y')


if __name__ == '__main__':
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    links = [a for a in soup.find_all('a') if '.pdf' in a.get('href', '').lower()]

    for link in links:
        href = link.get('href')
        url = BASE + href
        aria = link.get('aria-label', '').lower()

        if 'report' in aria:
            dt = parse_dt(aria)
            fout = f'{dt:%Y-%m}.pdf'
            print(fout)

            r = requests.get(url)
            with open(fout, 'wb') as f:
                f.write(r.content)

            delay = 3 + random.random() * 3
            print(f'sleeping for {delay}')
            time.sleep(delay)
