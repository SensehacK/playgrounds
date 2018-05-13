'''
Created on Mar 16, 2017

@author: venkata.goparaju
'''
import re
from database import ViewDB
username = ""
def Login():
    global username
    username = input("Enter the username:")
    password = input("Enter the password:")
    
# def security_question():
#     ans = input("What is your favourite hero's name:")
#     return ans

        
# def validate_password(password):
#     if (re.search(r'[A-Za-z]', password)!=None and re.search(r'\w\d', password)!=None and len(password)>=8):
#         print(password)
#         return  True
#     else:
#         return False
    
def check_username(name):
    list_of_usernames = ViewDB.validate_username(username)
    flag = False
    for names in list_of_usernames:
        if names[0] == name:
            flag = True
            return False
    if flag == False:
        return True

def insert_new_user(username):
    pass