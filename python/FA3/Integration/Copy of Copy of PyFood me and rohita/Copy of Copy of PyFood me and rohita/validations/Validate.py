'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from database import ViewDB,searchdb
from exceptions import CustomException2 

def validate_search_category(city,area): 
    list_of_search_categories=searchdb.search_as_a_guest(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidcityareaname()
    
        
    return list_of_search_categories
    
def validate_search_as_rating(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_likes(city,area): 
    list_of_search_categories=searchdb.search_as_likes(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
 
def validate_search_as_dislikes(city,area): 
    list_of_search_categories=searchdb.search_as_dislikes(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_dislikes(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating_dislikes(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2.Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_likes(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating_likes(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_type(city,area,rating_lower,rating_upper,var): 
    list_of_search_categories=searchdb.search_as_rating_type(city,area,rating_lower,rating_upper,var)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_dislike_like(city,area): 
    list_of_search_categories=searchdb.search_as_dislike_like(city,area)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_dislike_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_dislike_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_like_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_like_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_dislike_like(city,area,rating_lower,rating_upper): 
    list_of_search_categories=searchdb.search_as_rating_dislike_like(city,area,rating_lower,rating_upper)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_rating_dislike_type(city,area,rating_lower,rating_upper,var1): 
    list_of_search_categories=searchdb.search_as_rating_dislike_type(city,area,rating_lower,rating_upper,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_dislike_like_type(city,area,var1): 
    list_of_search_categories=searchdb.search_as_dislike_like_type(city,area,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_like_type_rating(city,area,rating_lower,rating_upper,var1): 
    list_of_search_categories=searchdb.search_as_like_type_rating(city,area,rating_lower,rating_upper,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_search_as_all(city,area,rating_lower,rating_upper,var1): 
    list_of_search_categories=searchdb.search_as_all(city,area,rating_lower,rating_upper,var1)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories

def validate_hotel_name(city,area,restaurant_name): 
    list_of_search_categories=searchdb.hotel_name(city,area,restaurant_name)
    if(len(list_of_search_categories)==0):
        raise CustomException2 .Invalidfilter()
    return list_of_search_categories
 
def validate_view_category(restaurant_type): 
    list_of_restaurant_categories=ViewDB.get_restaurant_categories(restaurant_type)
    if(len(list_of_restaurant_categories)==0):
        raise CustomException2 .InvalidCategoryException()
     
    return list_of_restaurant_categories
 
def validate_view_category_items(category): 
    list_of_restaurant_categories_items=ViewDB.get_categories_fooditems(category)
    if(len(list_of_restaurant_categories_items)==0):
        raise CustomException2 .InvalidCatItemsException
     
    return list_of_restaurant_categories_items
