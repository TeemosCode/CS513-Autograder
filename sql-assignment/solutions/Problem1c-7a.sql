select taken, person, quant, reading, v.site
from Visited v, Survey s
where v.id = s.taken and v.site='DR-1' and s.quant='rad'