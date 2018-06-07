select count(*) as count, avg(reading) as avg_temp
from Survey
where quant='temp' and person in ('pb')