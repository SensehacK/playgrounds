'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from utility import DBConnectivity
from classes.ItemModule3 import ItemCategories,CategoryItems

def get_restaurant_categories(restaurant_type) :
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants_categories=[]
        cur.execute("select fcid, categoryName, restaurant_type from FoodCategory where restaurant_Type=:restaurant",{"restaurant":restaurant_type})
        
        
        for fcid,categoryName,restaurant_type in cur:
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            ItemModule3=ItemCategories()
            ItemModule3.set_fcid(fcid)
            ItemModule3.set_category_name(categoryName)
            ItemModule3.set_restaurant_type(restaurant_type)           
            
            '''
            Here were are adding the product to a list
            '''
            list_of_restaurants_categories.append(ItemModule3)
            
        return list_of_restaurants_categories
    
    finally :
        cur.close()
        con.close()
        

def get_categories_fooditems(category) :
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants_fooditems=[]

        cur.execute("select ID,FoodName,Price,Availability,RestaurantFK,CategoryFK from FoodItem where CategoryFK=:category",{"category":category})
        
        for ciid, foodName, price, availability, restaurantFK, categoryFK in cur:
            
            '''
            In this loop, we are creating a product object for every row
            and setting the values from the row into the product object
            '''
            ItemModule3=CategoryItems()
            ItemModule3.set_ciid(ciid)
            ItemModule3.set_food_name(foodName)
            ItemModule3.set_price(price)
            ItemModule3.set_availability(availability)
            ItemModule3.set_restaurant_fk(restaurantFK)
            ItemModule3.set_category_fk(categoryFK)   
            
            '''
            Here were are adding the product to a list
            '''
            list_of_restaurants_fooditems.append(ItemModule3)
            
        return list_of_restaurants_fooditems
        
        
        
    finally :
        cur.close()
        con.close()
    