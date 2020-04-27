'''
Created on Feb 14, 2017

@author: kautilya.save
'''



names = ['Amir', 'Barry', 'Chales', 'Dao']
print(names[-1][-1])


names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
print(id(names1))
print(id(names2))
print(id(names3))
sum = 0
for ls in (names1, names2, names3):
    print(ls)
    print(ls[0])
    if ls[0] == 'Alice':
        sum += 1
    
    if ls[1] == 'Bob':
        sum += 10
    if ls[2] == 'Chales':
        print(sum)
    print(sum)
    
    
    
    
    
    
    
    
    
names1 = ['Amir', 'Barry', 'Chales', 'Dao']
if 'Amir' in names1:
    print(1)
else:
    print(2)
    
    

