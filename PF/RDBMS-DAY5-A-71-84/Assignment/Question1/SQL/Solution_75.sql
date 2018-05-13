select q.itemcode , sname , sum(or.qtyordered) as TotalQuantity
from quotation q inner join orders or 
on q.quotationid = or.quotationid 
group by q.itemcode, sname 
having sum(or.qtyordered) >= 100