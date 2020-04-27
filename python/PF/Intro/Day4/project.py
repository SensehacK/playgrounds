def message(input):
    
    
    variable_a = "a"
    
    #morse_words_list=[]
    
    for i in range(0,len(input)):
        j = i
        for key in my_dict:
           #print(my_dict[key])
            print(key)
            if input[j:j+3]==key:
                
                print("input[j:j+3]")
                print(input[j:j+3])
                
                morse_words_list.append(my_dict[key])
                j = j + 3
                continue
                
            elif input[j:j+2]== key:
                #print(key)
                morse_words_list.append(my_dict[key])
                j = j + 2
                
                
            elif input[j:j+1] != key :
                #morse_words_list.append("x")
                j = j + 1  
            else : 
                j = j + 1
                print("")
                #print("else block")
    print("return")
    return morse_words_list    
morse_words_list=[]
my_dict = {".." : "a", "..-" : "b", "-.." : "c"}
#morse_string = message("....")    
input="..-..-"    
morse_string = message(input)
print(morse_words_list)

