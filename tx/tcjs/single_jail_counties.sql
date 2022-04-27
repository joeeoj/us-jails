WITH ids_by_county AS (
SELECT
    county
    ,GROUP_CONCAT(id SEPARATOR ',') as ids
    ,COUNT(*) as cnt
FROM jails
WHERE
    facility_state = 'TX'
    AND NOT LOCATE(',', county) -- filter out multi-county rows
GROUP BY county
)

-- use output to create dict in county_mapping.py
SELECT *
FROM ids_by_county
WHERE cnt = 1
ORDER BY county
