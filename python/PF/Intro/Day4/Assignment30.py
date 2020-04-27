#PF-Assgn-30

def encode(message):   
    range1 = len(message)
    print("range1")
    print(range1)
    output = ""
    count = 1
    
    if range1 == 1 :
        output = str(count) + message
    else :
        for i in range(0 , range1-1) :

            if (message[i] == message[i+1]):
                count += 1
                i += 1
                
            elif(message[i] != message[i+1]): 
                output = output + str(count) + message[i]
                i += 1
                count = 1
            
            output = output + str(count) + message[i]
            #print(str_count + "" + str_i)
    return output    

    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("AAAAAABBBBCCCCCCCCAB")
print(encoded_message)