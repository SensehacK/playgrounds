'''
Created on Jan 23, 2017

@author: kautilya.save
'''



str_1 = 'Kautilya'
str_2 = "Sensehack"
str_3 = '''Save'''

print(str_1, str_2 , str_3)

str_1 = str_2 + str_3 

print(str_1)
str_2
if 'a' in str_1 :
    print("Found an 'A'")
else :
    print("Didnt found")



my_list = ["Kas", "sag", "saf"]
print(my_list)
print(my_list[1][2])

my_list[2] = "save"
print(my_list)

#Cant edit Strings in list but can append , Strings are immutable
#my_list[1][1] = "utilya"
print(my_list)




# Max ,  min functions 

my_numbers = [12,132345,34242,3235,43232,244]
print("max(my_numbers)")
print(max(my_numbers))

print("min(my_numbers)")
print(min(my_numbers))

print("sum(my_numbers)")
print(sum(my_numbers))


'''Cant Sort or max / min different types of strings & ints
my_numbers2 = [12,23,'13','ksara',43232,244]
print("max(my_numbers2)")
print(max(my_numbers2))

'''

message="welcome to Mysore"
word=message[-7:]
print(word)

message=message[3:14]
print(message)