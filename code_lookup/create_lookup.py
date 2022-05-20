from collections import defaultdict
import csv
import json


COMBOS = [
    ('FACID', 'ID'),
    ('FACID', 'JURISID'),
    ('FACID', 'GID'),
]


if __name__ == '__main__':
    with open('38323-0001-Data.tsv') as f:
        csvreader = csv.DictReader(f, delimiter='\t')
        data = [row for row in csvreader]

    for row in COMBOS:
        a, b = row
        fout = f'{a}_to_{b}.json'.lower()
        output = {d[a]: d[b] for d in data}

        with open(fout, 'wt') as f:
            json.dump(output, f, indent=2)

    output = defaultdict(list)
    for row in data:
        output[row['JURISID']].append({
            'ID': row['ID'],
            'FACID': row['FACID'],
            'GID': row['GID'],
            'COUNTY': row['COUNTY'],
            'FACNAME': row['FACNAME'],
            'RATED': row['RATED'],
        })

    with open('jurisid_to_many.json', 'wt') as f:
        json.dump(output, f, indent=2)

    output = defaultdict(list)
    for row in data:
        output[row['FACID']].append({
            'ID': row['ID'],
            'JURISID': row['JURISID'],
            'GID': row['GID'],
            'COUNTY': row['COUNTY'],
            'FACNAME': row['FACNAME'],
            'RATED': row['RATED'],
        })

    with open('facid_to_many.json', 'wt') as f:
        json.dump(output, f, indent=2)

    output = defaultdict(list)
    for row in data:
        output[row['CNTYFIPS']].append({
            'FACID': row['FACID'],
            'ID': row['ID'],
            'JURISID': row['JURISID'],
            'GID': row['GID'],
            'COUNTY': row['COUNTY'],
            'FACSTATE': row['FACSTATE'],
            'RUNAME': row['RUNAME'],
            'FACNAME': row['FACNAME'],
            'RATED': row['RATED'],
        })

    with open('cntyfips_to_many.json', 'wt') as f:
        json.dump(output, f, indent=2)
