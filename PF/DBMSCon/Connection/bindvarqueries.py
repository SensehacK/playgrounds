'''
Created on Mar 14, 2017

@author: kautilya.save
'''
import cx_Oracle
con = cx_Oracle.Connection('t753423/t753423@10.123.79.57/georli02')
cur = cx_Oracle.Cursor(con)
cur.execute("select * from employee where salary > :sal" , {"sal" : 32000})
print(cur.rowcount)
for var in cur :
    print(var)
cur.close()
con.commit()
con.close()