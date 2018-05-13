
--select max(salary) from empdetails where designation in ( select designation from empdetails )

--select designation from empdetails group by designation


--select max(e1.salary) , e1.empname  from empdetails e1 join empdetails e2
--on e1.empname = e2.empname where e1.designation in 
--(select designation from empdetails group by designation) 

select empname from empdetails em where salary = 
( select max(salary) from empdetails e where e.designation = em.designation)

--select empid,empname,designation,salary from empdetails em where 
--salary= (select max(salary) from empdetails e where e.designation=em.designation)
