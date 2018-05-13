#PF-Assgn-33

def find_common_characters(msg1,msg2):
    temp= ""
    timer=0
    for i in msg1:
        count = 0
        for j in msg2:
            if i == " ":
                break
            elif i == j:
                for k in temp:
                    if i == k:
                        count = count + 1
                if count == 0:
                    temp = temp + i
                    timer = timer+1
                else:
                    break
    if timer >=1:
        return temp
    else:
        return(-1)

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language" 
common_characters=find_common_characters(msg1,msg2)
print(common_characters)