select taken,person,quant, reading as corrected_reading from survey where (reading > 0.0 and reading < 1.0) and quant='sal' and (
person is null or person !='roe')
union
select taken,person,quant, reading/100 as corrected_reading from Survey s where s.person='roe' and quant='sal'