'''
Created on Mar 9, 2017

@author: Anbarasi.Ayyannan
'''
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('t753423/t753423@10.123.79.57/georli02')

def create_cursor(con):
    return cx_Oracle.Cursor(con)