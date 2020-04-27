'''
Created on Feb 19, 2017

@author: kautilya.save
'''



import re
if(re.search(r"Air","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    

if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
if(re.search(r"A\dl","A4line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
    
if(re.search(r"A[4-8]l","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    

if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    

if(re.search(r"Air\s","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
    
if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

if(re.search(r"A\d+","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
if(re.search(r"A\d?i","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
if(re.search(r"A\d{3}i","A223irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
if(re.search(r"^A","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
if(re.search(r"e$","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
    
if(re.search(r"\*","Air*line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")