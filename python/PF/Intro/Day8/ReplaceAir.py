'''
Created on Jan 30, 2017

@author: kautilya.save
'''
import re

str = "Jumabo Airlines a32323"
print (str.replace("a", "A", -1))

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print ("list1[3]: ", list1[3])
print ("list2[1:5]: ", list2[4:7])


flight_details3="Flight Savana Airlines a2134"
print(re.sub(r"Flight",r"Plane",flight_details3))


flight_details2="Flight Savana Airlines a2134"
print(re.sub(r"a(\d{4})",r"A\1",flight_details2))

flight_details="Flight Savana Airlines a2138"

if(re.search(r"Airlines",flight_details)!=None):
    print("Match Found: Airlines")
else:
    print("Match Not Found")

if(re.search(r"a2138$",flight_details)!=None):
    print("Match Found: a2138")
else:
    print("Match Not Found")

if(re.search(r"^F",flight_details)!=None):
    print("Match Found: Message starts with 'F'")
else:
    print("Match Not Found")


if(re.search(r"F..",flight_details)!=None):
    print("Match Found: Word starts with F and two consecutive characters")
else:
    print("Match Not Found")

if(re.search(r"\bSav\b",flight_details)!=None):
    print("Match Found:Word with blank spaces on both sides")
else:
    print("Match Not Found")

if(re.search(r"\d$",flight_details)!=None):
    print("Match Found: Message ends with number")
else:
    print("Match Not Found")

print("Word replaced in the message:")
print(re.sub(r"Flight","Plane",flight_details))
print("Word replaced in the message:")
print(re.sub(r"a(\d{4})",r"A\1",flight_details))
                                          