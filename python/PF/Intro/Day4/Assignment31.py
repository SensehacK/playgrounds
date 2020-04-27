#PF-Assgn-31
def check_palindrome(word):
    
    temp = ""
    
    for i in range(len(word),0 , -1) :
        temp = temp + word [i-1]
        
        print(word[i-1])
        
        
    if (temp == word) :
        print(word)
        return True
    else : 
        return False
    
    
    status  = check_palindrome("malayalam")
    
    if status : 
        print("Palindrome")
    else : 
        print("Not palindrome")
    
    
#                     length_word = len(word)
#                     count  = 0
#                     
#                     if length_word % 2 != 0 :
#                         middle = (length_word//2)+1 
#                         i = middle - 1 
#                         j = middle + 1
#                         
#                     else :
#                         i = (length_word//2)
#                         j = (length_word//2)
#                     
#                     temp = 0
#                     
#                     while temp < length_word // 2 :
        
    
    
    
    #Remove pass and write your logic here
    
   
   
   
   
   
#     if count == length_word // 2 :
#         return True
#     else :
#         return False

    


   
    
    
    
    
    
status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")