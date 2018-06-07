select distinct site as site
from Visited v, Survey s, Person p
where v.id = s.taken and p.personal='Frank' and s.person = p.id