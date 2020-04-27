#PF-Assgn-40
def is_palindrome(word):
    #Remove pass and write your logic here
    if len(word) <= 1:
        return True
    return word[0].upper() == word[-1].upper() and is_palindrome(word[1:-1])
    
#Provide different values for word and test your program       
result=is_palindrome("MADAM")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")