select taken,person,quant, reading/100 as reading
from Survey s
where s.person='roe' and quant='sal'