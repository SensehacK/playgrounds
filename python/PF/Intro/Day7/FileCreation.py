'''
Created on Jan 27, 2017

@author: kautilya.save
'''
try :
    flight_file=open("kautilya.txt","w")
    #flight_file.write("Hello Sensehack , KS,gh")
    text = flight_file.read()
    print(text)
    
except :
    print("File error")
finally:
    print("File close")
    flight_file.close()