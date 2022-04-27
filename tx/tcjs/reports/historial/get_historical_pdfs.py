import datetime
from pathlib import Path
import random
import time

import bs4
import requests
from tqdm import tqdm


URL = 'https://www.tcjs.state.tx.us/historical-population-reports/#1570704194976-460daca6-0a41'
PREFIX = 'https://www.tcjs.state.tx.us/wp-content/uploads'

FULL_MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
# full and abbreviations
MONTHS = dict(zip(FULL_MONTH, range(1, 13))) | dict(zip([m[:3] for m in FULL_MONTH], range(1, 13)))
MONTHS['Sept'] = 9  # outlier


def parse_year_month_from_href(href: str) -> str:
    p = Path(href)

    if 'Abbreviated' in href:
        *_, month, year = p.name.replace('.pdf', '').replace('_', '-').split('-')
        year = year[:4] if len(year) == 5 else year  # a few have an extra number at the end
        month = f'{MONTHS.get(month):02}'  # convert back to str
    elif 'AbbreRptCurrent' in href:
        *_, year, month = str(p.parent).split("/")
    return f'{year}-{month}'


if __name__ == '__main__':
    soup = bs4.BeautifulSoup(requests.get(URL).content, 'html.parser')
    links = [a for a in soup.find_all('a') if a.get('href', '').startswith(PREFIX) and a.get('target') == '_blank']

    for link in tqdm(links):
        url = link.get('href')
        year_month = parse_year_month_from_href(url)
        fout = f'{year_month}.pdf'

        r = requests.get(url)

        if r.status_code == 200:
            with open(fout, 'wb') as f:
                f.write(r.content)
            time.sleep(3 + random.random() * 3)
        else:
            print(r.status_code)
            print(url)
