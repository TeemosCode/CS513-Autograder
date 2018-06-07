select distinct c.cited as cited_but_not_in_Publication
from Cites c
where c.cited not in (select distinct pid from Publication )