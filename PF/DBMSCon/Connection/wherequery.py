'''
Created on Mar 14, 2017

@author: kautilya.save
'''
import cx_Oracle
con = cx_Oracle.Connection('t753423/t753423@10.123.79.57/georli02')
cur = cx_Oracle.Cursor(con)
cur.execute("SELECT * FROM Computer")
list1 = []
# for v in list1 :
#     print(v)
for row in cur:
    list1.append(row)
    print(row)
    
print(list1)
print(cur.rowcount)
cur.close()
# con.commit()
con.close()