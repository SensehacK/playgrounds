--select * from orders;

--
--select qtyordered from orders where status = 'Delivered';
--
--select * from item ; 


--select * from orders where qtyordered > 50 ;


--select descr,price from item where Reorderlevel = 150 ;

select descr , price from item where descr like '% Hard Disk %' ;