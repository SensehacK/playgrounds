select * from quotation;

--select * from quotation where qstatus = 'Closed'

--select sname , quotedprice as "Average quoted price" from quotation where  quotedprice > 500 and  qstatus = 'Closed'


--select sname , avg(quotedprice) as "Average quoted price" from quotation group by sname where avg(quotedprice) > 500 and qstatus = 'Closed' ;