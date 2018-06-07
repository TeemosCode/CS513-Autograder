select p.pid as citing, p2.pid as cited, p.year as citing_pub_year, p2.year as cited_pub_year
from Publication p, Publication p2,
(select distinct c.citing, c.cited
from Cites c, Cites c2
where c.citing = c2.cited) Cite
where Cite.citing=p.pid and Cite.cited=p2.pid and p.year < p2.year