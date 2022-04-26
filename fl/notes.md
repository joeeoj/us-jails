PDFs with monthly inmate populations by jail here:

http://www.dc.state.fl.us/pub/jails/index.html

## download_pdfs.py

iterate through root page and download all pdfs

## parsing

* Use Tabula to convert to csv
* Clean up with pandas and export into a single csv to be ingested into `inmate_population_snapshots`
* Manually create mapping from facility name to facility ID (id in `jails`)
* remove missing ids for now
* fix some typos in `jails`
