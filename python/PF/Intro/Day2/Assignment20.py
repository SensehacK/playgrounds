#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    approved = 0
    
    #Start writing your code here
    
    
    
    #Populate the variables: eligible_loan_amount and bank_emi_expected 
 
    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number) 
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)
    
    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work
    
    
    if loan_type == "Car" and salary > 25000 and salary <= 50000 :
        eligible_loan_amount = 500000
        bank_emi_expected = 36
        approved = 1
         
       
    elif loan_type == "House" and salary > 50000 and salary < 75000 :
        eligible_loan_amount = 6000000
        bank_emi_expected = 60
        approved = 1
    
    elif loan_type == "Business" and salary > 75000  :
        eligible_loan_amount = 7500000
        bank_emi_expected = 84
        approved = 1
         
         
         
         
    if approved == 1 :
        if account_number > 1000 and account_number <= 1999 :
            if account_balance >= 100000 :
                if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected :
                    
                    '''
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected )
                    print("Requested EMIs:", customer_emi_expected)
                    '''
                    
                    print("Account number:", account_number) 
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                    #Account number: 1005The customer can avail the amount of Rs. 500000Eligible EMIs : 36Requested loan amount: 300000Requested EMIs: 30 
                else :
                    print("The customer is not eligible for the loan ")
            else :
                print("Insufficient account balance")
        else :
            print("Invalid account number")  
    else :
        print("Invalid loan type or salary")
#Test your code for different values and observe the results

calculate_loan(1001,40000,250000,"Car",300000,30)


print("Hello2")
calculate_loan(1005,30000,255000,"Car",300000,30)
print("Hello4")
calculate_loan(1005,25000,255000,"Car",300000,30)

