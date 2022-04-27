import datetime
import random
import time

import requests


# these are snapshots as of the first day of the month so use that for the date
URL = 'https://www.tcjs.state.tx.us/wp-content/uploads/{year}/{month}/AbbreRptCurrent.pdf'
PAST_YEARS = [2021, 2020]  # goes back to 2020 by trial and error
TODAY = datetime.date.today()
COMBOS = []


if __name__ == '__main__':
    # current year
    for month in range(1, TODAY.month + 1):
        COMBOS.append((str(TODAY.year), f'{month:02}'))

    for year in PAST_YEARS:
        for month in range(1, 13):
            COMBOS.append((str(year), f'{month:02}'))

    for year, month in COMBOS:
        r = requests.get(URL.format(year=year, month=month))

        if r.status_code == 200:
            fout = f'{year}-{month}.pdf'

            with open(fout, 'wb') as f:
                f.write(r.content)

            delay = 3 + random.random() * 3
            print(f'delaying for {delay:.2} seconds')
            time.sleep(delay)
