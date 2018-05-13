select i1.itemcode , descr from item i1 
join quotation q1 on i1.itemcode = q1.itemcode 
where q1.qstatus in ('Closed', 'Rejected') 
and   q1.quotedprice >= ( select max(q2.quotedprice ) from quotation q2 
where q2.qstatus in ('Closed', 'Rejected') ) 




select * from emp

select * from vehicle

select * from empvehicle

desc employee

select * from employee

select designation from employee having count(designation) > 1

select count(designation) from employee where designation in ('PM', 'SE')
select count(designation) from employee where designation in ('PM')










select * from employee e1 join employee e2 on e1.designation = e2.designation and e1.id = e2.id where e1.designation in ( select designation from employee group by designation having count(*) >= 1 )

 group by designation having count(*) > 1 ;
select * from employee

select ename,salary from employee order by salary desc

select ename,salary,bonus ,dept , doj from employee order by dept, doj









select ename from employee where designation = ( select designation from employee where count(designation) > 1 )



select ename , empno from emp 
where empno in (select empno from empvehicle where vehicleid = (select vehicleid from empvehicle group by vehicleid having count(*) > 1))


select vehicleid from empvehicle group by vehicleid having count(*) > 1