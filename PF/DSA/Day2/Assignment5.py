#DSA-Assgn-5

#This assignment needs DataStructures.py file in your package, you can get it    from resources page
from DataStructures import LinkedList

def create_new_sentence(word_list):
    new_sentence=""
    new_word = ""
    present_node = word_list.get_head()
    next_node = present_node.get_next()
    
    
    while present_node.get_next() is not None :
        print(present_node.get_data())
        print(next_node.get_data())
        
        if ( present_node.get_data() == "*" or present_node.get_data() == "/") and (next_node.get_data() == "*" or  next_node.get_data() == "/") :
            print("hello")
            new_word = new_word + " "
            present_node = next_node.get_next()
            next_node = present_node.get_next()
            new_word = new_word + present_node.get_data().upper()
           
        elif (present_node.get_data() == "*" or present_node.get_data() == "/") and (next_node.get_data() != "*" or  next_node.get_data() != "/") :
            
            new_word = new_word + " "
        
        else :
            new_word = new_word + present_node.get_data()
            
            
        present_node  = present_node.get_next()
        next_node = next_node.get_next()
        print(present_node.get_data())
        #print(next_node.get_data())
            
    new_word = new_word + present_node.get_data()
    new_sentence = new_word
    
    return new_sentence

word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")


result=create_new_sentence(word_list)
print(result)