'''
Created on Mar 17, 2017

@author: komal.preet
'''
from classes.FoodModule import Food
class Billing:
    username = Food.registered_user
    is_registered_user = Food.is_registered_user
    chosen_restaurant = ""
    food_ordered = []
    food_item_list = []
    items_not_available = []
    total_charge = 0
    discount = 0
    ans = ""
    payment_ans = ""
    rating_ans = 0
    like_ans = ""
    updated_likes = 0
    updated_dislikes = 0
    card_number = ""
    cvv_number = 0
    expiry_date = ""
    name_on_card = ""
    grid_card_number = ""
    start_billing_ans = ""
    
#     def __init__(self):
#         self.__chosen_restaurant = ""
#         self.food_ordered = []
#         self.food_item_list = []
#         self.items_not_available = []
#         self.__total_charge = 0
#         self.__discount = 0
#         self.__ans = ""
#         self.__payment_ans = ""
#         self.__rating_ans = 0
#         self.__like_ans = ""
#         self.__updated_likes = 0
#         self.__updated_dislikes = 0
#         self.__card_number = ""
#         self.__cvv_number = 0
#         self.__expiry_date = ""
#         self.__name_on_card = ""
#         self.__grid_card_number = ""
#         self.__start_billing_ans = ""
# 
#     
# 
#     def get_chosen_restaurant(self):
#         return self.__chosen_restaurant
#     def get_food_ordered(self):
#         return self.food_ordered
#     def get_food_item_list(self):
#         return self.food_item_list
#     def get_items_not_available(self):
#         return self.items_not_available
#     def get_total_charge(self):
#         return self.__total_charge
#     def get_discount(self):
#         return self.__discount
#     def get_ans(self):
#         return self.__ans
#     def get_payment_ans(self):
#         return self.__payment_ans
#     def get_rating_ans(self):
#         return self.__rating_ans
#     def get_like_ans(self):
#         return self.__like_ans
#     def get_updated_likes(self):
#         return self.__updated_likes
#     def get_updated_dislikes(self):
#         return self.__updated_dislikes
#     def get_card_number(self):
#         return self.__card_number
#     def get_cvv_number(self):
#         return self.__cvv_number
#     def get_expiry_date(self):
#         return self.__expiry_date
#     def get_name_on_card(self):
#         return self.__name_on_card
#     def get_grid_card_number(self):
#         return self.__grid_card_number
#     def get_start_billing_ans(self):
#         return self.__start_billing_ans
# 
# 
#     def set_chosen_restaurant(self, value):
#         self.__chosen_restaurant = value
#     def set_food_ordered(self, value):
#         self.food_ordered = value
#     def set_food_item_list(self, value):
#         self.food_item_list = value
#     def set_items_not_available(self, value):
#         self.items_not_available = value
#     def set_total_charge(self, value):
#         self.__total_charge = value
#     def set_discount(self, value):
#         self.__discount = value
#     def set_ans(self, value):
#         self.__ans = value
#     def set_payment_ans(self, value):
#         self.__payment_ans = value
#     def set_rating_ans(self, value):
#         self.__rating_ans = value
#     def set_like_ans(self, value):
#         self.__like_ans = value
#     def set_updated_likes(self, value):
#         self.__updated_likes = value
#     def set_updated_dislikes(self, value):
#         self.__updated_dislikes = value
#     def set_card_number(self, value):
#         self.__card_number = value
#     def set_cvv_number(self, value):
#         self.__cvv_number = value
#     def set_expiry_date(self, value):
#         self.__expiry_date = value
#     def set_name_on_card(self, value):
#         self.__name_on_card = value
#     def set_grid_card_number(self, value):
#         self.__grid_card_number = value
#     def set_start_billing_ans(self, value):
#         self.__start_billing_ans = value