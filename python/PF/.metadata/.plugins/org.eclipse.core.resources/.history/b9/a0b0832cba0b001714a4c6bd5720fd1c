'''
Created on Mar 17, 2017

@author: komal.preet
'''
from utility import DBConnectivity
from classes.BillingModule4 import Billing
from classes import FoodModule
this_username=Billing.username
this_restaurant=Billing.chosen_restaurant

'''0'''
def db_start_billing():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("delete from CheckoutCart where username = :username",{"username":this_username})
        
    finally :
        con.commit()
        cur.close()
        con.close()
    
'''0.5'''
def db_check_for_empty():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        check = 0
        cur.execute("select quantity from CheckoutCart where username = :username",{"username":this_username})
        for i in cur:
            check = i
        return check
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''1'''
def db_fetching_chosen_restaurant():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        print(username)
        cur.execute("select restaurant_name from CheckoutCart where username = :username",{"username":this_username})
        for restaurant_name in cur:
            Billing.chosen_restaurant=restaurant_name[0]
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''2.5'''
def db_display_cart():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select foodname,quantity from CheckoutCart where username = :username",{"username":this_username})
        print()
        print("[ITEM NAME]  [QUANTITY]")
        for foodname,quantity in cur:
            print(foodname,"          ",quantity)
            Billing.food_ordered.append(foodname)
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''3'''
def db_fetching_items_available():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        a="A"
        cur.execute("select foodname from fooditem where restaurant_name=:restaurant_name and availability=:a",{"restaurant_name":this_restaurant,"a":a})
        for foodname in cur:
            print(foodname[0])
            Billing.food_item_list.append(foodname[0])
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''6'''
def db_processing_unavailable_items():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        for i in Billing.items_not_available:
            cur.execute("delete from checkoutcart where username = :username and foodname = :foodname",{"username":this_username,"foodname":i})
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''8'''
def db_updating_total_price():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("update checkoutcart set total_price = quantity * price where username = :username",{"username":this_username})
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''9'''
def db_display_full_cart():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select foodname,quantity,price,total_price from CheckoutCart where username = :username",{"username":this_username})
        print()
        print("[ITEM NAME]  [QUANTITY] [PRICE] [TOTAL_PRICE]")
        for foodname,quantity,price,total_price in cur:
            print(foodname,"         ",quantity,"       ",price,"    ",total_price)
            print()
    finally :
        con.commit()
        cur.close()
        con.close()
           
'''10'''
def db_calculating_total_charge():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select sum(total_price) from CheckoutCart where username = :username group by username",{"username":this_username})
        for i in cur:
            Billing.total_charge=i[0]
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''12'''
def db_if_door_deliver():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con) 
        delivery_charges = 0   
        cur.execute("select DOOR_DELIVERY_CHARGES from Restaurants where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant})
        for j in cur:
            delivery_charges = j[0]
        return delivery_charges
    finally :
        con.commit()
        cur.close()
        con.close()
        
'''15,16'''
def db_deleting_after_payment():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con) 
        cur.execute("delete from checkoutcart where username = :username",{"username":this_username})
    finally :
        con.commit()
        cur.close()
        con.close()
        
'''15,16'''
def db_updating_transection_table():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con) 
        cur.execute("select order_count from User_Transactions where username = :username",{"username":this_username})
        for i in cur:
            user_count = i[0]
        user_count+=1
        cur.execute("update User_Transactions set order_count = :user_count where username = :username",{"username":this_username,"user_count":user_count})
        
        cur.execute("select overall_total_price from User_Transactions where username = :username",{"username":this_username})
        for j in cur:
            overall_total_price = j[0]
        overall_total_price+=Billing.total_charge
        cur.execute("update User_Transactions set overall_total_price = :overall_total_price where username = :username",{"username":this_username,"overall_total_price":overall_total_price})
        
    finally :
        con.commit()
        cur.close()
        con.close()
            
'''18'''
def db_take_feedback_first():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select likes from Restaurants where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant})
        for i in cur:
            Billing.updated_likes=i[0]+1
        cur.execute("update Restaurants set likes =:updated_likes where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant,"updated_likes":Billing.updated_likes})
        
    finally :
        con.commit()
        cur.close()
        con.close()
                    
                    
'''18'''
def db_take_feedback_second():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select dislikes from Restaurants where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant})
        for i in cur:
            Billing.updated_dislikes=i[0]+1
        cur.execute("update Restaurants set dislikes =:updated_dislikes where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant,"updated_dislikes":Billing.updated_dislikes})
    finally :
        con.commit()
        cur.close()
        con.close()
                    
'''18'''
def db_update_rating(rating_ans):
    try:
        rating = 0
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("select rating from Restaurants where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant})
        for i in cur:
            rating = i[0]  
            
       
        new_rating = (float(rating_ans)+rating)/2
        print(new_rating)
        cur.execute("update Restaurants set rating = :new_rating where RESTAURANTNAME=:restaurantname",{"restaurantname":this_restaurant,"new_rating":new_rating})
        
        
    finally :
        con.commit()
        cur.close()
        con.close()
    