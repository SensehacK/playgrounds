'''
Created on Mar 14, 2017

@author: kautilya.save
'''
import cx_Oracle
con = cx_Oracle.Connection('t753423/t753423@10.123.79.57/georli02')
cur = cx_Oracle.Cursor(con)

year1 = input("Enter Year:")
make1 = input("Enter Make:")
cur.execute("SELECT * FROM Computer where myear > "+year1 + "and make = " +"'" +make1 + "'")
for row in cur:
    print(row)
print(cur.rowcount)
cur.close()
# con.commit()
con.close()