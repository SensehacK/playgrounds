'''
Created on Mar 17, 2017

@author: kautilya.save
'''

from utility import DBConnectivity
from validations import Validate

def display_details():
    print("*********************************************")
    print("         Welcome to Display Details !!! ")
    print("*********************************************")
    
    print()
    print("Please Select from the below menu ")
    print()
    
    print("a. Display most rated hotel")
    print("b. Display the customer details")
    print("c. Display city wise hotel details")
    print()
    
    display_details_choice()
    
    
def display_details_choice():
    
    dd_choice = input("Your Choice : ")
    
    if(dd_choice.lower()=="a"):
        print("Your selected choice : a" )
        display_most_rated_hotel()
            
    elif(dd_choice.lower()=="b"):
        print("Your selected choice : b" )
        max_user = display_most_ordered_transactions_user()
        print("The highest transactions made by a customer is " , max_user)
        
    elif(dd_choice.lower()=="c"):
        print("Your selected choice : c" )
        display_highest_booked_hotel_by_city()

    else:
        print("Please enter a valid input (a,b,c or A,B,C)")
        #Calling back function
        display_details_choice()
    




def display_most_rated_hotel():
    
    print("In Function def display_most_rated_hotel():")
    list_of_restaurants=Validate.validate_highest_rated()
    print("resturantname","\ttype of food","\tlikes" ,"\tdislikes","\trating")
    for select in list_of_restaurants:
        print(select.get_restaurantname(),"\t",select.get_type_of_food(),"\t",select.get_likes(),"\t",select.get_dislikes(),"\t",select.get_rating())
    print()

    
    
    
    
    

    

def display_most_ordered_transactions_user():
    print("In Function display_most_ordered_transactions_user")
    
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        max_transact_user = ""
        
        '''User Query
        #select username from User_Transactions where order_count = ( select max(order_count) from User_Transactions);
        '''
        
        cur.execute("select username from User_Transactions where order_count = ( select max(order_count) from User_Transactions)")

        for username in cur :
            #print(username)
            max_transact_user  = username[0]
            
        
        return max_transact_user
    
    finally :
        print("Closing the cursor & connections in (def display_most_ordered_transactions_user)")
        cur.close()
        con.close()
    


def display_highest_booked_hotel_by_city():
    print("In Function display_highest_booked_hotel_by_city")
    city1=input("Enter city name:")
    city=city1.upper()
    list_of_restaurants=Validate.validate_city_wise_highest_booked(city)
    print("resturantname","\t","city","\t","area","\t","rating")
    for select in list_of_restaurants:
        print(select.get_restaurantname(),"\t",select.get_city(),"\t",select.get_area(),"\t",select.get_rating())
    print()

    