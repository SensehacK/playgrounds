'''
Created on Jan 25, 2017

@author: kautilya.save
'''


def tower_of_hanoi(n, source,destination,temp):
    if(n==1):
        disk=source.pop(0) #Removes the element in specified position
        print("if(n==1):")
        print(disk)
        destination.insert(0,disk) #Inserts the given element in specified position
        return
    
    print(" tower_of_hanoi(n-1) before")
    tower_of_hanoi(n-1, source, temp, destination)
    print("tower_of_hanoi(n-1) after ")
    print("disk=source.pop(0)")
    disk=source.pop(0)
    print(disk)
    destination.insert(0,disk)
    tower_of_hanoi(n-1, temp, destination, source)
    return

source=["blue","green","orange"]
destination=[]
temp=[]
tower_of_hanoi(3, source, destination, temp)
print("Source:",source)
print("Destination:",destination)