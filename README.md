# US Jail and Prison Inmate Records and Incidents

The world has its eyes on US corrections. We lock up more people than any other country, with [573 people in prison per 100,0000](https://www.prisonpolicy.org/reports/pie2022.html) nationwide. Data on individual prisons is tough to come by, but a number of projects have data science teams working on finding it. We're taking a step in the direction of transparency by crowdsourcing the data collection and making the database open-source. We're leaning heavily on the data that's out there, and hope that our bounty participants can find troves of interesting data. The sources may be used in future projects as well.

With the data that we find we can:
* get a clear picture of what kind of public-facing information exists
* track prison incidents (suicides/deaths)
* look at jails that systematically hold onto large numbers of unconvicted people
* jumpstart other projects that depend on the scraped inmate data

Right now we are only looking at aggregate data (total populations, not inmate-level.)

## Bounty rules

(To ensure fairness, the rules may be updated in certain circumstances.)

1. PRs are reviewed in order of last updated
1. If a PR is accepted it is merged immediately
1. If a PR has mistakes it is closed immediately, but a grace period may be given under some circumstances
1. PR descriptions must outline the changes made by the PR (empty or vague descriptions may lead to a closed PR)
1. Snapshots must be a month apart at minimum (see below)
1. You *are* allowed to add to the `jails` table *if* you check first that your jail is not present

## `snapshot_date`

To level the playing field between datasets I am not allowing daily snapshots: some cities/states publish daily prison statistics, which can skew the dataset towards single locations and disincentivize further scraping. **Inmate count snapshots must be a month apart at minimum.**

If the snapshot date represents a day, simply put that date in the cell.

But suppose you are given the number of prison inmates in a given period, use the last day in the reporting period.

**EXAMPLE**: If the record spans a **month**, say from Jan 1, 2019 to Feb 1, 2019, make the `date_reported = '2019-02-01'`. 

**EXAMPLE**: If the report spans a **year**, say from Jan 1, 2019 to Jan 1, 2020, make the `date_reported = '2020-01-01'`.

Monthly or yearly averages are fine, if that's all that's provided.

## `start_date` and `end_date` in the incidents table

Just use the ranges given in the dataset to frame the incidents.

## `source_url` and `source_url_2`

You *must* have a source URL, but sometimes there's a need for an additional source URL. You can use this second column if needed.

## the `jails` table

If you're sure that the jail you've found is not in the table, you can add it. The `jails` table [comes from a 2019 census](https://www.icpsr.umich.edu/web/NACJD/studies/38323/)

## Bounty schema

You can view the schema by doing `dolt schema show` or going to the bounty webpage. However there is one important thing to know: **in the initial stages of the bounty the schemas of `inmate_population_snapshots` and `incidents` may change** to accommodate the data that you all discover. In the first week or so of the bounty we can consider adding columns to the incidents and inmate population tables.