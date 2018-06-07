select p1.*
from Publication p1, Publication p2
where p1.pid = p2.pid 
and (
p2.authors!= p1.authors or
p2.year != p1.year or
p2.title != p1.title or
p2.journal != p1.journal or
p2.vol != p1.vol or
p2.no != p1.no or
p2.fp != p1.fp or
p2.lp != p1.lp or
p2.publisher != p1.publisher
)