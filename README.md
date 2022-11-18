# SQL Builder
This is an example of using the builder design pattern to create an SQL builder using Python.

## Usage
In python:
```
from AdvancedSQLBuilder import AdvancedSQLBuilder

print(
    AdvancedSQLBuilder().SELECT("NAME").SELECT("COUNT(*)")
    .FROM("CAR_SALES")
    .START_DATE("SELL_DATE", '2021-11-18 00:00:00')
    .END_DATE("SELL_DATE", '2022-11-18 00:00:00')
    .ORDER_BY("COUNT(*)")
    .GROUP_BY("NAME")
    .BUILD()
)
```
Outputs:
```
DECLARE @start_date datetime = 2021-11-18 00:00:00
DECLARE @end_date datetime = 2022-11-18 00:00:00

SELECT NAME, COUNT(*)
FROM CAR_SALES
WHERE 1=1
AND SELL_DATE is not null
AND SELL_DATE >= @start_date
AND SELL_DATE is not null
AND SELL_DATE < @end_date
GROUP BY NAME
ORDER BY COUNT(*)
```
