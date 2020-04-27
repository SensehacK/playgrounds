'''
Created on Mar 17, 2017

@author: komal.preet
'''
import datetime

def ValidateCardNumber(card_number):
    card_number_final = ""
    for i in range(0,len(card_number)):
        if i!=4 and i!=9 and i!=14:
            card_number_final = card_number_final + card_number[i]    
    if card_number_final.isdigit() and len(card_number_final)==16:
        card_number_validate = True
    else:
        print("Invalid Card Number.")
        card_number_validate = False
    return card_number_validate

def ValidatecvvNumber(cvv_number):
    cvv_number_str = str(cvv_number)
    if cvv_number_str.isdigit() and len(cvv_number)==3:
        cvv_number_validate = True
    else:
        print("Invalid CVV Number.")
        cvv_number_validate = False
    return cvv_number_validate

def ValidateCardName(card_name):
    if card_name.isalpha():
        card_name_validate = True
    else:
        print("Invalid Card-holder Name.")
        card_name_validate = False
    return card_name_validate

def validateExpiryDate(expiry_date):
    exp_date_list=[]
    present_date_list=[]
    if "/" in expiry_date:
        exp_date_list = expiry_date.split("/")
        if len(exp_date_list[1]) == 2:
            exp_date_list[1]="20"+exp_date_list[1]
        exp_year = int(exp_date_list[1])
        exp_month = int(exp_date_list[0])
    
        if exp_month <= 12:
            present_date = str(datetime.date.today())
            present_date_list = present_date.split("-")
            present_year = int(present_date_list[0])
            present_month = int(present_date_list[1])
        
            if exp_year>present_year and exp_month>= present_month:
                expiry_date_validate=True
            else:
                print("Invalid Expiry Date.")
                expiry_date_validate=False
        else:
            print("Invalid Expiry Date.")
            expiry_date_validate=False
    else:
        print("Invalid Expiry Date.")
        expiry_date_validate=False
        
    return expiry_date_validate