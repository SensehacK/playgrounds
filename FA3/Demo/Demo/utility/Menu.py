'''
Created on Jul 29, 2015

@author: Deepak_M05
'''
'''
This module displays a menu to the user.
'''

from functionality import ViewFunctions


print("Welcome to Online Shopping!!")
print("***************************************")

print("Choose an option from below:\n")

end=False

'''
This loop runs till the user enters 3
'''
while(end==False):
    print("1. View Products")
    print("2. Purchase a product")
    print("3. Exit")
    option=input()
    if(option.isdigit() and (int(option)>=1 and int(option)<=3)):
        if(int(option)==1):
            print("View Products")
            ViewFunctions.view_product()
        if(int(option)==2):
            print("Purchase Product")
    
        if(int(option)==3):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3 )")
    
