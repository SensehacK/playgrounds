select ename , dname from emp e1 join
dept d1 on e1.deptno = d1.deptno 
where job = 'MANAGER'