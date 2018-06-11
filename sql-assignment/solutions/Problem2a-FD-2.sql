select p1.journal, p1.publisher
from Publication p1
where p1.journal in (  select distinct journal from Publication group by journal having count(distinct(publisher)) > 1 )