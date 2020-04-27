'''
Created on Mar 16, 2017

@author: gaurav.sainger

'''
from utility import DBConnectivity
from classes.ItemModule3 import ItemCategories,CategoryItems
from classes.searchmodule2 import Select


def search_as_a_guest(city,area):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category and area=:category1",{"category":city,"category1":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
            select=Select()
            select.set_restaurantname(restaurantname)
            select.set_type_of_food(type_of_food)
            select.set_likes(likes)
                      
            select.set_dislikes(dislikes)
            select.set_rating(rating)
           
            list_of_restaurants.append(select)
            
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()
        
def search_as_rating(city,area,rating_lower,rating_upper):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]

        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and rating between :category and :category1",{"category":rating_lower,"category1":rating_upper,"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
            select=Select()
            select.set_restaurantname(restaurantname)
            select.set_type_of_food(type_of_food)
            select.set_likes(likes)               
            select.set_dislikes(dislikes)
            select.set_rating(rating)
          
            list_of_restaurants.append(select)
            
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()
        
def search_as_likes(city,area):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]

        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 order by likes desc",{"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
          
            select=Select()
            select.set_restaurantname(restaurantname)
            select.set_type_of_food(type_of_food)
            select.set_likes(likes)               
            select.set_dislikes(dislikes)
            select.set_rating(rating)
           
            list_of_restaurants.append(select)
            
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()
        
           
def search_as_dislikes(city,area):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]

        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 order by dislikes",{"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
            select=Select()
            select.set_restaurantname(restaurantname)
            select.set_type_of_food(type_of_food)
            select.set_likes(likes)               
            select.set_dislikes(dislikes)
            select.set_rating(rating)
          
            list_of_restaurants.append(select)
            
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()        


def search_as_type(city,area,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]

        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and type_of_food like :category",{"category":'%'+var1+'%',"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
            select=Select()
            select.set_restaurantname(restaurantname)
            select.set_type_of_food(type_of_food)
            select.set_likes(likes)               
            select.set_dislikes(dislikes)
            select.set_rating(rating)
            
            list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
def search_as_rating_dislikes(city,area,rating_lower,rating_upper):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and rating between :category and :category1 order by dislikes",{"category":rating_lower,"category1":rating_upper,"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
        
def search_as_rating_likes(city,area,rating_lower,rating_upper):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and rating between :category and :category1 order by likes desc",{"category":rating_lower,"category1":rating_upper,"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
def search_as_rating_type(city,area,rating_lower,rating_upper,var):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and rating between :category and :category1 and type_of_food like :category3",{"category":rating_lower,"category1":rating_upper,"category3":'%'+var+'%',"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()  
def search_as_dislike_like(city,area):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 order by likes desc, dislikes asc",{"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
def search_as_dislike_type(city,area,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and type_of_food like :category order by dislikes ",{"category":'%'+var1+'%',"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()  

def search_as_like_type(city,area,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and type_of_food like :category order by likes desc",{"category":'%'+var1+'%',"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()
        
def search_as_rating_dislike_like(city,area,rating_lower,rating_upper):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and rating between :category and :category1 order by likes desc ",{"category":rating_lower,"category1":rating_upper,"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
        
def search_as_rating_dislike_type(city,area,rating_lower,rating_upper,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and rating between :category and :category1 and type_of_food like :category3 order by dislikes ",{"category":rating_lower,"category1":rating_upper,"category3":'%'+var1+'%',"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
        
def search_as_dislike_like_type(city,area,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and type_of_food like :category order by likes desc,dislikes",{"category":'%'+var1+'%'})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close() 
         
def search_as_like_type_rating(city,area,rating_lower,rating_upper,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and type_of_food like :category and rating between :category2 and :category3 order by likes desc",{"category":'%'+var1+'%',"category2":rating_lower,"category3":rating_upper,"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()
        
def search_as_all(city,area,rating_lower,rating_upper,var1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from restaurants where city=:category4 and area=:category5 and type_of_food like :category and rating between :category2 and :category3 order by likes desc,dislikes asc",{"category":'%'+var1+'%',"category2":rating_lower,"category3":rating_upper,"category4":city,"category5":area})
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()
        
def hotel_name(city,area,restaurant_name):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
#         print("restaurant_name")
#         print(restaurant_name)
        cur.execute("select restaurantname from restaurants where city=:category4 and area=:category5 and restaurantname=:category",{"category":restaurant_name,"category4":city,"category5":area})
        
        for restaurantname in cur:
                print("restaurant def hotel_name(city,area,restaurant_name):")
                print(restaurant_name)
                select=Select()
                select.set_restaurantname(restaurantname)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()          
                          
        
                                 
                                              
                          
def search_highest_rated():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select restaurantname,type_of_food,likes,dislikes,rating from (select restaurantname,type_of_food,likes,dislikes,rating from restaurants order by rating desc) where rownum < 6")
        
        for restaurantname,type_of_food,likes,dislikes,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_type_of_food(type_of_food)
                select.set_likes(likes)               
                select.set_dislikes(dislikes)
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
        cur.close()
        con.close()  
        
def city_wise_highest_booked(city):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        list_of_restaurants=[]
        
        cur.execute("select t.restaurantname, t.city, t.area, t.rating from restaurants t WHERE T.CITY =:category AND t.rating in(select max(u.rating) from restaurants u where u.city =:category group by u.city)",{"category":city})
        
        for restaurantname,city,area,rating in cur:
            
                select=Select()
                select.set_restaurantname(restaurantname)
                select.set_city(city)
                select.set_area(area)
                
                select.set_rating(rating)
            
                list_of_restaurants.append(select)   
        return list_of_restaurants
    
    finally:
       cur.close()
       con.close()  
        
              
        
                       
               
                        
        
             
                
                
        
        