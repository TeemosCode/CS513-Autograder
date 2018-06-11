select name,lat,long,dated,personal,family,quant,reading
from Visited v, Survey s, Person p, Site si
where v.id = s.taken and s.person = p.id and si.name = v.site
and v.dated is not null 
order by v.dated