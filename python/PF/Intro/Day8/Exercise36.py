'''
Created on Jan 30, 2017

@author: kautilya.save
'''
#PF-Tryout
import re

flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

#This function returns the values in the search result
def printout(search_result):
    if(search_result!=None):
        return search_result.group()
    else:
        return "No Output"

search_result = re.search(r"British Airways", flight_details) 
print(printout(search_result))

search_result = re.search( r"16:45$" , flight_details)
print(printout(search_result))

search_result = re.search(r"^Good", flight_details)
print(printout(search_result))

search_result = re.search(r"F.{5}",flight_details) 
print(printout(search_result))


print(re.sub(r"ba(\d{4})", r"BA\1" ,flight_details))
print(flight_details)
                                          