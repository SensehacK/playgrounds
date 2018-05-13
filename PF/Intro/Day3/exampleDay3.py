


passenger = "SP"
for passenger in "A","A", "FC", "C", "FA",  "SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue  
        
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
         
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
        
    print("Check the person")
    print("Check for cabin baggage")

















baggage_count=10
no_of_baggage_picked=0
while(baggage_count>0):
    no_of_baggage_picked = (int)(input ("Number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
    print("No. of baggage remaining:",baggage_count)
    



i1 = 1
i2 =  "$"

for i in range (1,9) :
    
    i1 += 1
    for k in range (i) :
        print("",i2,end = "")
    print("")
    