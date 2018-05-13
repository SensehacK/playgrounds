SELECT dname from dept d1 join emp e1 on
d1.deptno = e1.deptno 
where sal > 1500
group by dname having count(dname) > 1