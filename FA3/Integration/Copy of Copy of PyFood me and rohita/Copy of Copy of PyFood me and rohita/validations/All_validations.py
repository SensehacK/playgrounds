'''
Created on Mar 17, 2017

@author: rohita
'''
import re
from exceptions.Input_exceptions import InvalidUserNameException, InvalidEmailException, PhoneNumberException, InvalidPasswordException, AlreadyExistingPasswordException
from database import ViewDB

def validate(username):
    try:
        if len(username) != 0:
            return True
        else:
            raise InvalidUserNameException()
        
    except InvalidUserNameException as e:
        print(e)
        return False


def validate_phone_number(phone_no):
    try:
        if (re.search(r'[0-9]', phone_no)!=None and len(phone_no) == 10):
            return True
        else:
            raise PhoneNumberException()
    
    except PhoneNumberException as e:
        print(e)
        return False

def validate_email(emailid):
    try:
        if (re.search(r'(\w+[.|\w])*@(\w+[.])*(com$|in$)', emailid) != None):
            return True
        
        else:
            raise InvalidEmailException()
        
    except InvalidEmailException as e:
        print(e)
        return False

def validate_existing_password(username,password):
    try:
        print(ViewDB.existing_password(username,password))
        print(ViewDB.existing_password(username,password)[0])
        if password != ViewDB.existing_password(username,password)[0]:
            return True
        else:
            raise AlreadyExistingPasswordException()
        
    except AlreadyExistingPasswordException as e:
        print(e)
        return False


def validate_password(password):
    try:
        if (re.search(r'[A-Za-z]', password)!=None and re.search(r'\w\d', password)!=None and len(password)>=8):
            print(password)
            return True
        else:
            raise InvalidPasswordException()
        
    except InvalidPasswordException as e:
        print(e)
        return False