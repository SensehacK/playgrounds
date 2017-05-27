'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from utility import DBConnectivity
from classes.ItemModule3 import ItemCategories,CategoryItems
from classes import FoodModule


def get_restaurant_categories(restaurant_name) :
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants_categories=[]
        
        
        cur.execute("select unique category_name from fooditem where restaurant_name=:rest_name",{"rest_name":restaurant_name})
        
        '''
        print("In function /get_restaurant_categories")
        print("executing the query for categories")
        print("Printing the tuples from query cursor directly")
        '''
        
        for category in cur :
            #print(category)
            list_of_restaurants_categories.append(category[0])
        
        print(list_of_restaurants_categories)
        
        return list_of_restaurants_categories
    
    finally :
        print("Closing the cursor & connections in (def get_restaurant_categories)")
        cur.close()
        con.close()
        

def get_categories_fooditems(restaurant_name , category_name) :
    try:
        print("///////////////////////////////////////")
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants_fooditems=[]
        
        #Debugging prints
#         print("Created cursors & now executing them")
#         print(restaurant_name)
#         print(type(category_name))
#         print(category_name)

        cur.execute("select foodname , price , availability from fooditem where restaurant_name =:restaurant_n and category_name =:category_n",{"restaurant_n":restaurant_name, "category_n":category_name })

        print("After execute")
        for  foodName, price, availability in cur:
            
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            ItemModule3=CategoryItems()
            ItemModule3.set_food_name(foodName)
            ItemModule3.set_price(price)
            ItemModule3.set_availability(availability)
            
            '''
            #Printing the items from tupples directly in  get_categories_fooditems
            print("Printing the items from tupples directly in  get_categories_fooditems")
            print(foodName , price, availability)
            '''
            
            '''
            Here were are adding the FoodItems to a list
            '''
            list_of_restaurants_fooditems.append(ItemModule3)   

        return list_of_restaurants_fooditems

    finally :
        cur.close()
        con.close()
        
        
def get_food_items_availability(selected_food_items) :
    try:
        print("///////////////////////////////////////")
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_food_items_availability=[]
        restaurant_name = FoodModule.Food.restaurant_name
        
        #Debugging prints
        print("Created cursors & now executing them")
        print(selected_food_items)
        print(type(selected_food_items))

        
        
        for food_items in selected_food_items :
            cur2=DBConnectivity.create_cursor(con)
            cur2.execute("select availability from fooditem where foodname =:food_n and restaurant_name =:restaurant_n" , {"food_n" :food_items, "restaurant_n" : restaurant_name})
            
            for val in cur2 :
                print(val)
                list_of_food_items_availability.append(val[0])

        
        print("After execute")
            
        '''
        In this loop, we are creating a product object for every row
        and setting the values from the row into the product object
           
           redundant code
           
           if "NA" in list_of_food_items_availability :
            return False
        else :
            return True
        '''
        
        print("list_of_food_items_availability")
        print(list_of_food_items_availability)
        return list_of_food_items_availability
        
        
        

    finally :
        cur.close()
        con.close()


def get_selected_food_items_present(selected_food_items) :
    try:
        print("///////////////////////////////////////")
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_selected_food_items_present=[]
        restaurant_name = FoodModule.Food.restaurant_name
        
        #Debugging prints
        print("Created cursors & now executing them")
        print(selected_food_items)
        print(type(selected_food_items))

        
        
        for food_items in selected_food_items :
            cur2=DBConnectivity.create_cursor(con)
            cur2.execute("select foodname from fooditem where foodname =:food_n and restaurant_name =:restaurant_n" , {"food_n" :food_items, "restaurant_n" : restaurant_name})
            
            for val in cur2 :
                print(val)
                list_of_selected_food_items_present.append(val[0])

        
        print("After execute")
        
        print("list_of_selected_food_items_present")
        print(list_of_selected_food_items_present)
        return list_of_selected_food_items_present
        
        
        

    finally :
        cur.close()
        con.close()
    