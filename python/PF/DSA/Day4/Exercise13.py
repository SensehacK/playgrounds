'''
Created on Feb 13, 2017

@author: kautilya.save
'''
#DSA-Tryout

import random

def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
    
    low = 0
    high = len(element_list) -1
    flag = False
    while low <= high :
        mid = (low+high)//2
        
        if num == element_list[mid] :
            print("Element found")
            flag = True
            break
            
        elif num > element_list[mid] :
            low = mid + 1
        
        else :
            high = mid - 1
    
    

    if flag :
        print("Element found at " , mid)
    else :
        print("Element not found")       
        
    return mid
#Initializes a list with values 1 to n in ascending order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    # Remove pass and write the code to implement the above three steps.
    list1 = initialize_list_of_elements(n)
    r_num = random.randrange(1,n+1)
    print(find_it(r_num, list1))
    
    
#Pass different values to play() and observe the output
play(100)