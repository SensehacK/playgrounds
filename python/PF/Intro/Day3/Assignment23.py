#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    not_available = 0
    #Write your logic here
    
    gem_overall_price = 0
    
    for i in range (0 , len(reqd_gems)) :
        print("////////////////////////////////////////////////////")
        print("For Loop first start")
        
        for j in range (0 , len(gems_list)) :
            print("For Loop second start")
            
            if reqd_gems[i] == gems_list[j]:
                not_available = not_available + 1
                #Found one & multipy the required quantity with price list
                print("Required Gems")
                print(reqd_gems[i])
                print("Gem List")
                print(gems_list[j])
                print("Gem Price")
                print(price_list[j])
                print("Gem Quantity")
                print(reqd_quantity[i])
                
                gem_overall_price = price_list[j] * reqd_quantity[i]
                print("gem_overall_price")
                print(gem_overall_price)
                
                print("bill_amount before ")
                print(bill_amount)
                
                bill_amount = gem_overall_price + bill_amount
                
                print("bill_amount after")
                print(bill_amount)
                print("End of if statement")
                
            
                
        print("For Loop second end")  
        
        
        
    if bill_amount > 30000 :
        print("/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/")
        print("bill_amount > 30000 ")
        new_discount_amount = bill_amount * (5/100)
        
        
        print("After 5% discount  amount")
        print(new_discount_amount)
        
        print("After discount Total Bill  amount")
        new_discounted_total_bill_amount  = bill_amount - new_discount_amount
        print(new_discounted_total_bill_amount)
        
        bill_amount = new_discounted_total_bill_amount
    
    '''else :
                print("Else statement condition of if")
                not_available = 1
                '''
    if not_available == 0 and not_available < len(reqd_gems) :
        bill_amount = -1
    
    
    print("For Loop first end")
    
    return bill_amount

#List of gems available in the store            
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)