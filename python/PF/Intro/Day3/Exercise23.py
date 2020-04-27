#PF-Exer-23
def translate(bilingual_dict,english_words_list):
    #Write your logic here
    list1 = []
    list2 = []
    for keys,values in bilingual_dict.items():
        list1.append(keys)
        list2.append(values)
    
    
    for v in zip (list1, list2) :
        print(v)
    
    for i in list1 :
        print(i)
        
    for j in list2 :
        print(j)
    
    
    print(list1)
    print(list2)
    #return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)