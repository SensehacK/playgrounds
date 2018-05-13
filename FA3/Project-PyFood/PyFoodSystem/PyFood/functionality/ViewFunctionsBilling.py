'''
Created on Mar 17, 2017

@author: komal.preet
'''
from database import ViewDBbilling
from classes.BillingModule4 import Billing
from validations import ValidateBilling

'''0'''
def start_billing():
    check=check_for_empty()
    if check == 0:
        print("Your cart is empty.!")
    else:
        print("Do you want to Bill, Cancel or Save for later? (B/C/S) :")
        Billing.start_billing_ans=input()
        start_billing_ans = Billing.start_billing_ans
        if start_billing_ans.upper() == "B":
            fetching_chosen_restaurant()
            check_for_empty()
        elif start_billing_ans.upper() == "S":
            print("Your data has been saved in the cart. Thank you and come back soon!")
        elif start_billing_ans.upper() == "C":
            ViewDBbilling.db_start_billing()
            print("Your data has been deleted. Thank you and come back soon!")
        else:
            print("You have entered an invalid entry. Kindly chose again.")
            start_billing()
        
'''0.5'''
def check_for_empty():
    check = ViewDBbilling.db_check_for_empty()
    if check == 0:
        return 0
    else:
        return 1
    
'''1'''
def fetching_chosen_restaurant():
    ViewDBbilling.db_fetching_chosen_restaurant()
    display_first_line()
        
'''2'''
def display_first_line():
    print("Items ordered @ ",Billing.chosen_restaurant)
    display_cart()
    
'''2.5'''
def display_cart():
    ViewDBbilling.db_display_cart()
    fetching_items_available()
    checking_availability()
    if len(Billing.items_not_available) != 0:
        displaying_unavailable_items()
    else:
        dine_delivery()

'''3'''
def fetching_items_available():
    ViewDBbilling.db_fetching_items_available()
        
'''4'''
def checking_availability():
    for foodname in Billing.food_ordered:
        
        if foodname not in Billing.food_item_list:
            Billing.items_not_available.append(foodname)
            
'''5'''
def displaying_unavailable_items():
    print("Following item(s) in your cart are not available:-")
    for i in Billing.items_not_available:
        print(i)
    processing_unavailable_items()
    
            
'''6'''
def processing_unavailable_items():
    answer = "a"
    if len(Billing.food_ordered) == len(Billing.items_not_available):
        print("Will go to kautilya's function latter.")
    else:
        print("Do you want to continue billing without the unavailable item(s)? (Y/N)")
        answer=input()

    if answer.upper() == "Y":
        ViewDBbilling.db_processing_unavailable_items()
        dine_delivery()
    elif answer.upper() == "N":
        print("Will go to kautilya's function latter.")
    elif answer.upper() != "Y" and answer.upper()!= "N" and answer.upper() != "A":
        print("Invalid entry. Kindly enter again.")
        processing_unavailable_items()
        
'''7'''
def dine_delivery():
    print("You would like to dine-in(I) or door-delivery(D)?")
    Billing.ans=input()
    updating_total_price()
    calculating_total_charge()
    display_full_cart()
    checking_discount_eligibility()
    if Billing.ans.upper() == "D":
        if_door_deliver()
    elif Billing.ans.upper() == "I":
        pass
    else:
        print("Invalid entry. Kindly enter again.")
        dine_delivery()
    displaying_total_amount()
    fetching_payment_option()
    
'''8'''
def updating_total_price():
    ViewDBbilling.db_updating_total_price()
    
'''9'''
def display_full_cart():
    ViewDBbilling.db_display_full_cart()
    
    
'''10'''
def calculating_total_charge():
    ViewDBbilling.db_calculating_total_charge()
    
        
'''11'''
def checking_discount_eligibility():
    if Billing.is_registered_user == True:
        Billing.discount=0.05*Billing.total_charge
    else:
        Billing.discount = 0
    print("Discount = ",Billing.discount)
    Billing.total_charge=Billing.total_charge-Billing.discount
    
'''12'''
def if_door_deliver():
    delivery_charges = ViewDBbilling.db_if_door_deliver()
    Billing.total_charge+=delivery_charges
    print("Delivery charges = ",delivery_charges)
        
'''13'''
def displaying_total_amount():
    print("Total charge = ",Billing.total_charge)
    
'''14'''
def fetching_payment_option():
    print("Payment Option (cash/card): ")
    Billing.payment_ans=input()
    if Billing.payment_ans.lower() == "cash":
        if_cash()
    elif Billing.payment_ans.lower() == "card":
        if_card()
    else:
        print("Invalid entry. Kindly enter again")
        fetching_payment_option()

'''15'''
def if_cash():
    print("Amount paid successfully !")
    ViewDBbilling.db_updating_transection_table()
    ViewDBbilling.db_deleting_after_payment()
    take_feedback()
    
'''16'''
def if_card():
    print("Enter card number : ")
    Billing.card_number=input()
    print("Enter cvv number : ")
    Billing.cvv_number=input()
    print("Enter expiry date : ")
    Billing.expiry_date=input()
    print("Enter the name on card : ")
    Billing.name_on_card=input()
    print("Enter grid_card_number(H-I-K) : ")
    Billing.grid_card_number=input()
    if validate_card() == True:
        if Billing.card_number.startswith("4"):
            print("Card is valid! Type Visa")
            print("Amount paid successfully !")
        elif Billing.card_number.startswith("5"):
            print("Card is valid! Type MasterCard")
            print("Amount paid successfully !")
        elif Billing.card_number.startswith("6"):
            print("Card is valid! Type Rupay")
            print("Amount paid successfully !")
        else:
            print("Card is valid! Type 'others'")
            print("Amount paid successfully !")
    else:
        print("Invalid card. Please enter card details again.")
        if_card()
    ViewDBbilling.db_updating_transection_table()
    ViewDBbilling.db_deleting_after_payment()
    take_feedback()
    
'''17'''
def validate_card():
    card_number = Billing.card_number
    cvv_number = Billing.cvv_number
    card_name = Billing.name_on_card
    expiry_date = Billing.expiry_date
    
    card_number_validate = ValidateBilling.ValidateCardNumber(card_number)
    cvv_number_validate = ValidateBilling.ValidatecvvNumber(cvv_number)
    card_name_validate = ValidateBilling.ValidateCardName(card_name)
    expiry_date_validate = ValidateBilling.ValidateCardName(expiry_date)
    
    if card_number_validate and cvv_number_validate and card_name_validate and expiry_date_validate:
        return True
    else:
        return False
    

'''18'''
def take_feedback():
    print("Provide Rating: ")
    ratings=input()
    Billing.rating_ans=int(ratings)
    ViewDBbilling.db_update_rating(int(ratings))
    
    print("Did you like the service? (Y/N)")
    Billing.like_ans=input()
    
    if Billing.like_ans.upper() == "Y":
        ViewDBbilling.db_take_feedback_first()
        
        
    if Billing.like_ans.upper() == "N":
        ViewDBbilling.db_take_feedback_second()
    print("Thank you for you feedback. Have a nice day!")