select reading-(select avg(reading) from Survey where quant='rad') as 'reading-average'
from Survey
where quant='rad'