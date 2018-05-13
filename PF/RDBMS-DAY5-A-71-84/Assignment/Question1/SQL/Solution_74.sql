--The management of EasyShop would like to know the retail outlet ids and 
--the details like description, type and retail unit price of items whose retail unit price is 
--more than 1500.
--select * from item ;

--select * from retailstock


select rs.roid , it.descr , it.itemtype , unitprice from retailstock rs 
join item it on rs.itemcode = it.itemcode and unitprice > 1500
