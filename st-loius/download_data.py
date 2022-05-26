import calendar
import datetime
import json
import pathlib
import random
import time
import urllib

import bs4
import requests


DATE_FMT = '%m/%d/%Y'
BASE_URL = 'https://www.stlouis-mo.gov/data/dashboards/inmates/by-day.cfm?'
PARAMS = {
    'date': '04%2F30%2F2022',
    'race': 'all',
    'sex': 'all',
    'employment': 'all',
    'maritalStatus': 'all',
    'topCharge': 'all',
}
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
}
SESSION = requests.Session()


def format_date(dt: datetime.datetime) -> str:
    """Workaround because of double encoding error"""
    return  dt.date().strftime('%m/%d/%Y')


def table_to_dict(table_id: str) -> dict:
    table = soup.find('table', id=table_id).find('tbody')
    d = {}
    for row in table.find_all('tr'):
        label, count, pct = [td.text.strip() for td in row.find_all('td')]
        d[label] = int(count)
    return d


if __name__ == '__main__':
    urls = []
    for year in range(2000, 2023):
        for month in range(1, 13):
            params = PARAMS.copy()
            last_day = calendar.monthrange(year, month)[-1]
            dt = datetime.datetime(year, month, last_day)
            output_date = dt.strftime('%Y-%m-%d')
            fout = pathlib.Path('data') / f'{output_date}.json'

            # prevent re-downloads if I need to restart it
            if not fout.exists():
                params['date'] = format_date(dt)

                url = BASE_URL + urllib.parse.urlencode(params)
                urls.append(url)

                print(url)
                r = SESSION.get(url)
                soup = bs4.BeautifulSoup(r.content, 'html.parser')
                delay = 1 + random.random() * 2
                print(f'sleeping for {delay:.3f}')
                time.sleep(delay)

                total = int(soup.find("div", class_="stat-number").text.strip())
                sex = table_to_dict('SexTable')
                race = table_to_dict('RaceTable')
                offense = table_to_dict('OffenseTable')
                age_group = table_to_dict('AgeGroupTable')
                facility = table_to_dict('PopulationbyFacilityTable')

                d = {
                    'total': total,
                    'url': url,
                    'date': output_date,
                    'sex': sex,
                    'race': race,
                    'offense': offense,
                    'age_group': age_group,
                    'facility': facility,
                }

                with open(fout, 'wt') as f:
                    json.dump(d, f, indent=2)
