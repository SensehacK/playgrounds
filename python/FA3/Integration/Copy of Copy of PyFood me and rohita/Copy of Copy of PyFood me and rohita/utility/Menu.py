'''
Created on Mar 9, 2017

@author: Anbarasi.Ayyannan
'''
'''
This module displays a menu to the user.


'''

from functionality.filtersearch import search_as_guest
from functionality import Registration

print("*********************************************")
print("         Welcome to PyFood Service!! ")
print("*********************************************")
print("Choose an Option from below:\n")

end=False

while(end==False):
    print("1. Registration")
    print("2. Search Restaurant")
    print("3. Item Search")
    print("4. Billing")
    print("5. Display Details")
    print("6. Exit")
    option=input("Enter your choice:")
    if(option.isdigit() and (int(option)>=1 and int(option)<=6)):
        if(int(option)==1):
            print("Registration")
            Registration.register()
           
        if(int(option)==2):
            print("Search Restaurant")
            search_as_guest()
            
            
        if(int(option)==3):
            print("Item Search")
            
        if(int(option)==4):
            print("Billing")
            
        if(int(option)==5):
            print("Display Details")
            
        if(int(option)==6):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option (1,2,3,4,5,6)")
