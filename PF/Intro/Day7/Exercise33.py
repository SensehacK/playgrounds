#PF-Tryout
import random

def guess_number(number_in_mind):
    number = random.randrange(0,10)
    print(number)
    if number_in_mind > 10 :
        print("Properly Enter number")
    else :
        if (number < number_in_mind ):
            print ('Number is low')
        elif (number > number_in_mind ):
            print ('Number is high')
        elif (number == number_in_mind ):
            print ('You have got it right!!!')
        
#Provide different values for number_in_mind and test your program
guess_number(67)