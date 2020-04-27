#PF-Assgn-26
from tkinter.constants import RAISED

def solve(heads,legs):
    error_msg="No solution" 
    chicken_count=0
    rabbit_count=0
    
    
    raised = heads*2
    legdiff = legs - raised
    rabbit_count = legdiff//2
    chicken_count = heads-rabbit_count
    
    if legs%2 != 0 or legs < heads :
        print(error_msg)
    else:
        print(chicken_count,rabbit_count)
    
    if (legdiff==heads or rabbit_count == heads):
        rabbit_count=heads
        chicken_count=0
    else:
        rabbit_count=legdiff
        chicken_count=heads-rabbit_count            
    
    
    
    
    
    
    
    
    
    
    
    
    # Use the below given print statements to display the output 
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(400,1020)