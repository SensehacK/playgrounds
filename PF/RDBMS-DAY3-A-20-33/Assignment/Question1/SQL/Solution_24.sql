--select * from quotation , orders ;

select quotation.quotationid , orders.status , orders.orderid from quotation , orders where quotation.quotationid = orders.quotationID and orderdate between '01-Dec-2014' and '01-Jan-2015' ;