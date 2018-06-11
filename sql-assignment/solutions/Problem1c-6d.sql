select group_concat(Full_Name, ',') as full_names_list_last_name_ordered
from 
(select personal || ' ' || family as Full_Name
from Person order by family) p