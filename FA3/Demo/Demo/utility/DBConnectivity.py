'''
Created on Jul 29, 2015

@author: Deepak_M05
'''
import cx_Oracle
'''
Having the core DB operations in one place reduces rework and increases modularity
'''


def create_connection():
    return cx_Oracle.Connection('Your connection string')

def create_cursor(con):
    return cx_Oracle.Cursor(con)