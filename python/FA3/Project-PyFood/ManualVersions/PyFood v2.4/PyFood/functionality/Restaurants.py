'''
Created on Mar 17, 2017

@author: gaurav.sainger

'''
from functionality import filtersearch
def restaurants(city,area):
    city1=city.upper()
    area1=area.upper()
    
    
    filtersearch.search_as_login(city1, area1)
    