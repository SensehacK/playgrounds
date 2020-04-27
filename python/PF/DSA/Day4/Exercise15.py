#DSA-Exer-15

def pattern_search(text, pattern):
    length = len(pattern)
    count = 0
    
    for i in range (len(text)):
        if text [i:(i+ length)] == pattern :
            count += 1
        
 
    
    return count
    

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)