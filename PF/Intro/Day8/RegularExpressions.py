'''
Created on Jan 30, 2017

@author: kautilya.save
'''

import re


ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

air = []

for i in ticket_list :
    print(i)
    air = i.split(":")

print(air)
# if(re.search(r"^..(\d ){3}",air)!=None):
#     print("Match Found: ..567")
            
            