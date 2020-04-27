#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    list_text = text.split()
    unknown_words = []
    unknown_set = {}
    
    
    for value in list_text :
        is_value_present = False
        value_period = ""
        if "." in value :
            #print("Periods")
            value_period = value.replace("." , "")
        for voc in vocabulary :
            if value == voc or value_period == voc :
                    is_value_present = True
                    
        if not is_value_present :
            unknown_words.append(value)
        
    
    if len(unknown_words) == 0 :
        return -1
    
    unknown_set = set(unknown_words)
        
    return unknown_set
    
    
    
#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)