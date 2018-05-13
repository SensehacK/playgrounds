'''
Created on Mar 16, 2017

@author: venkata.goparaju
'''
from utility import DBConnectivity
# from validations import All_validations
from classes.RegistrationModule import Customer

def login(username,password):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select username,password,cityname,area from registration where username=:category1 and password=:category2",{"category1":username,"category2":password})
        for username,password,cityname,area in cur:
            '''
            In this loop, we are creating a registration object for every row
            and setting the values from the row into the registration object
            '''
            customer=Customer()
            customer.set_username(username)
            customer.set_password(password)
            customer.set_city(cityname)
            customer.set_area(area)
            
            '''
            Here were are adding the new registration to a list
            '''
            return customer
    
    finally:
        cur.close()
        con.close()
        

def security_question(username,answer):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select password from registration where username=:category1 and answer=:category2",{"category1":username,"category2":answer})
        for password in cur:
            customer=Customer()
            customer.set_password(password)
            
            return customer
        
    finally:
        cur.close()
        con.close()
        
        
def check_answer(username):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select answer from registration where username=:category1",{"category1":username})
        for answer in cur:
            '''
            In this loop, we are creating a registration object for every row
            and setting the values from the row into the registration object
            '''
            customer=Customer()
            customer.set_answer(answer)
            
            '''
            Here were are adding the new registration to a list
            '''
            return customer
    
    finally:
        cur.close()
        con.close()
        
        
def update_password(username,input2):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update registration set password =:input2 where username=:use",{"use":username,"input2":input2})
 
    finally:
        cur.close()
        con.commit()
        con.close()
        
def validate_username(username):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_name=[]
        cur.execute("select username from registration")
        for username in cur:
            '''
            In this loop, we are creating a registration object for every row
            and setting the values from the row into the registration object
            '''
            customer=Customer()
            customer.set_username(username)
             
            '''
            Here were are adding the new registration to a list
            '''
            list_of_name.append(username)
        return list_of_name
     
    finally:
        cur.close()
        con.close()
        
        
        
def insert_new_user(UserName,emailid,mobilenumber,password,question,answer,cityname,area,state):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("insert into registration values (:category1, :category2, :category3, :category4, :category5, :category6, :category7, :category8, :category9)" ,{"category1":UserName,"category2":emailid,"category3":mobilenumber,"category4":password,"category5":question,"category6":answer,"category7":cityname,"category8":area,"category9":state})
        
 
    finally:
        cur.close()
        con.commit()
        con.close()
        
def check_question(username):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select question from registration where username=:category1",{"category1":username})
        for question in cur:
            '''
            In this loop, we are creating a registration object for every row
            and setting the values from the row into the registration object
            '''
            customer=Customer()
            customer.set_question(question)
            
            '''
            Here were are adding the new registration to a list
            '''
            return customer
    
    finally:
        cur.close()
        con.close()

def existing_password(username,password):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_passwords=[]
        cur.execute("select password from registration where username=:category1",{"category1":username})
        for password in cur:
            '''
            In this loop, we are creating a registration object for every row
            and setting the values from the row into the registration object
            '''
            customer=Customer()
            customer.set_password(password)
            list_of_passwords.append(password)
            
            '''
            Here were are adding the new registration to a list
            '''
            return list_of_passwords[0]
    
    finally:
        cur.close()
        con.close()
        