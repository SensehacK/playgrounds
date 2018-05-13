
# from functionality import ViewFunctions
from functionality import ViewFunctions
from functionality import ViewFunctionsBilling

'''
This module displays a menu to the user.
'''
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
    option=input()
    if(option.isdigit() and (int(option)>=1 and int(option)<=6)):
        if(int(option)==1):
            print("Registration")
           
        if(int(option)==2):
            print("Search Restaurant")
            
        if(int(option)==3):
            print("Item Search")
            # Calling Module 3 Function classes Functions
            ViewFunctions.view_category()
            print("/./////////////................////////////////////")
            print("Back from the ViewFunctions.view_category()")
            
            
        if(int(option)==4):
            print("Billing")
            ViewFunctionsBilling.start_billing()
            
        if(int(option)==5):
            print("Display Details")
            
        if(int(option)==6):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option (1,2,3,4,5,6)")
