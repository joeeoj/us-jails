## Texas Commission on Jail Standards (TCJS)

https://www.tcjs.state.tx.us/population-reports/

* County Jail Population: https://www.tcjs.state.tx.us/wp-content/uploads/2022/04/AbbreRptCurrent.pdf
* Convert to csv with Tabula. Parse with jupyter and pandas.
* No reports for:
    * 2022-02
    * 2020-01 - FOUND it [here](https://www.tcjs.state.tx.us/wp-content/uploads/2020/07/Abbreviated_Pop_Rpt_Jan_2020.pdf) with the historical reports
* SJF = State Jail Felony
    * Type of crime in Texas, still a felony but least severe type of felony
    * https://www.shouselaw.com/tx/defense/felony/state-jail/
* Form jails use for reporting: https://www.tcjs.state.tx.us/wp-content/uploads/2019/10/Jail-Population-report-Printable.pdf

### older data (not parsed yet)

Historical reports back to 1992: https://www.tcjs.state.tx.us/historical-population-reports/#1570705032002-ee3f2291-7279

missing reports:

* https://www.tcjs.state.tx.us/wp-content/uploads/2019/08/Abbreviated-Pop-Rpt-Aug-2007.pdf
* https://www.tcjs.state.tx.us/wp-content/uploads/2019/08/Abbreviated-Pop-Rpt-Nov-2005.pdf
* https://www.tcjs.state.tx.us/wp-content/uploads/2019/08/Abbreviated-Pop-Rpt-Dec-2005.pdf
* https://www.tcjs.state.tx.us/wp-content/uploads/2019/08/Abbreviated-Pop-Rpt-July-2004.pdf
* https://www.tcjs.state.tx.us/wp-content/uploads/2019/08/Abbreviated-Pop-Rpt-Feb-2003.pdf

## parsing notes

* `total_contract` - I think this is contracting with with another county to house an inmate (because there is no space) so I'm interpreting this as offsite
    * https://statutes.capitol.texas.gov/Docs/LG/htm/LG.351.htm

### translating columns

`inmate_population_snapshots` -> pdf column

* total -> total_pop
* total_off_site -> total_contract
* felony -> convicted_felons
* misdemeanor -> convicted_misdemeanor
* technical_parole_violators
    * parole_violators
    * parole_violators_with_new_charge
* federal_offense -> federal
* convicted_or_sentenced
    * convicted_felons
    * convicted_felons_sentenced_to_county_jail_time
    * convicted_misdemeanor
    * convicted_sjf_sentenced_to_county_jail_time
    * convicted_sjf_sentenced_to_state_jail_time
* detained_or_awaiting_trial
    * pretrial_felons
    * pretrial_misdemeanor
    * pretrial_state_jail_felony

Problem is most of these don't add up to the total pop. This means either numbers are incorrectly reported or more likely double counting is happening. If that's the case the numbers can be reported as is, though they are confusing.

## sources for new `jails` entries

not added yet

* Anderson County Jail
    * https://www.inmateaid.com/prisons/anderson-county-tx-jail
* Aransas County Detention Center
    * https://www.aransascounty.org/detentioncenter/
* Bailey County Jail
    * https://www.inmateaid.com/prisons/bailey-county-tx-jail
    * https://laurelcorrections.com/texas/county-jail/bailey-county-jail/
* Baylor County Jail
    * https://prisonroster.com/prisons/texas/county-jail/baylor-county-jail/
    * http://texasjailroster.com/county-sheriff/baylor-county/
    * https://hcsheriff.org/texas/county-jail/baylor-county-jail/
