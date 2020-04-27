#PF-Assgn-46
import numbers
def nearest_palindrome(number):
    number = number + 1
    while(1) :
        num1 = str(number)
        if num1 == (str(number)[::-1]) :
            return int(num1)
        else :
            number += 1
number=12300
print(nearest_palindrome(number)) 


        