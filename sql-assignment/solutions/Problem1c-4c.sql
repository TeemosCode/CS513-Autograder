select distinct substr(name, 0, instr(name,'-')) as site
from Site s