'''
Created on Mar 9, 2017

@author: Anbarasi.Ayyannan
'''
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('t753406/t753406@10.123.79.56/georli01')

def create_cursor(con):
    return cx_Oracle.Cursor(con)