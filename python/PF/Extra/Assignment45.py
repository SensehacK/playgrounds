#PF-Tryout
def find_armstrong(number):
    original_number = number # save original number here
    temp=0
    while(number!=0):
        remainder=number%10
        number=number//10 # perform integer division
        temp+=(remainder*remainder*remainder)
    if(original_number==temp): # compare with the original number
        return True            # because num has been modified
    return False
        
number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")  
else:
    print(number,"is not an Armstrong number")