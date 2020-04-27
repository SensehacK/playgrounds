'''
Created on Mar 17, 2017

@author: venkata.goparaju
'''
# If the username is already existing in the database
class InvalidUserNameException(Exception):
    def __init__(self):
        super().__init__("The Username cannot be empty, please relogin")
  
# If the password is already existing in the database
class AlreadyExistingPasswordException(Exception):
    def __init__(self):
        super().__init__("The password already exists, please check and relogin")

  
# If the password entered by the user is not valid
class InvalidPasswordException(Exception):
    def __init__(self):
        super().__init__("The password you have entered is not valid, please check your password and relogin")
    
# If the phone number is invalid
class PhoneNumberException(Exception):
    def __init__(self):
        super().__init__("The phone number you have entered is invalid, please re-login by entering the correct phone number")
    
# If the email is not valid
class InvalidEmailException(Exception):
    def __init__(self):
        super().__init__("The email you have entered is invalid, Plese re-login by entering the correct email")
    