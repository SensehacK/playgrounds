

--select sname from quotation group by itemcode

select sname from quotation where quotedprice < (
select max(quotedprice) from quotation group by quotedprice )