'''
Created on Mar 13, 2017

@author: kautilya.save
'''
from time import sleep
from threading import Thread
gas_remaining=2 # in liters
def cook():
    global gas_remaining
    if gas_remaining>0:
        print("Cooking")
        sleep(2)
        gas_remaining-=2
        print("Gas after cooking ",gas_remaining)
if __name__ == '__main__':
    Thread(target=cook).start()
    Thread(target=cook).start()