import datetime
import json

import bs4
import requests


URL = 'http://www.dc.state.fl.us/pub/jails/index.html'
BASE = 'http://www.dc.state.fl.us/pub/jails/'


if __name__ == '__main__':
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    links = [a for a in soup.find_all('a') if '.pdf' in a.get('href', '').lower()]

    output = {}
    for link in links:
        aria = link.get('aria-label', '')
        if aria:
            dt = datetime.datetime.strptime(aria.lower().replace('report', '').strip(), '%B %Y')
            url = BASE + link.get('href')

            output[dt.strftime('%Y-%m')] = url

    with open('url_mapping.json', 'wt') as f:
        json.dump(output, f, indent=2)
