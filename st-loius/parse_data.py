import csv
import glob
import json


JAILS = {
    "St. Louis City Justice Center": 8155,
    "St. Louis Medium Security Institution": 8156,
    "St. Louis City Jail": 8125,
}
HEADER = ['id', 'snapshot_date', 'total']


if __name__ == '__main__':
    results = []
    for fname in glob.glob('./data/*.json'):
        with open(fname) as f:
            data = json.load(f)

        snapshot_date = data.get('date')
        total = data.get('total')
        url = data.get('url')

        for fac, total in data.get('facility').items():
            d = {
                'id': JAILS.get(fac),
                'snapshot_date': snapshot_date,
                'total': total,
                'source_url': url,
            }
            results.append(d)

    with open('inmate_population_snapshots.csv', 'wt') as f:
        csvwriter = csv.DictWriter(f, fieldnames=results[0].keys())
        csvwriter.writeheader()
        csvwriter.writerows(results)
