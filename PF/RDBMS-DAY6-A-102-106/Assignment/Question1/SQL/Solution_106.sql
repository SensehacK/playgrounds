select custid , custname "CUSTNAME" from customer c1 where not Exists( 
select custid from purchasebill where c1.custid = custid )