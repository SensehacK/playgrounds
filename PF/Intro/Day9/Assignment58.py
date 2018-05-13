#PF-Assgn-58
def validate_credit_card_number(card_number):
    credit_card_str = str(card_number)
    sum = 0
    for i in range(len(credit_card_str)):
        if i%2 == 0 :
#             print("i:", i)
#             print(credit_card_str[i])
            value = int(credit_card_str[i]) * 2
            sum+=value %10 + value // 10
        else : 
            sum+=int(credit_card_str[i])
            
    return sum%10 == 0

      
card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")


