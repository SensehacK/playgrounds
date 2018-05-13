#PF-Assgn-48
def find_correct(word_dict):
    answer_list = []
    right_count = 0
    almost_correct_count = 0
    wrong_count = 0
    for keys , values in word_dict.items() :
        count_not_same = 0
        count_same = 0
        i1 = 0
        if len(keys) != len(values) :
            wrong_count += 1
        else : 
            for i in keys : 
                if keys[i1] == values[i1] :
                    count_same += 1
                else :
                    count_not_same += 1
                i1 += 1
            if count_same == len(keys) :
                    right_count += 1
            elif count_not_same <= 2 :
                    almost_correct_count += 1
            elif count_not_same > 2 :
                    wrong_count += 1
    answer_list.append(right_count)
    answer_list.append(almost_correct_count)
    answer_list.append(wrong_count)
    
    return answer_list

word_dict = {"POLICY":"POLICY", "WIND": "WIPE", "WELCOME": "WELL"}
#word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}  
print(find_correct(word_dict))