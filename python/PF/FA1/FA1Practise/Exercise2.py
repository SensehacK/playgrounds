names1 = ['Amir', 'Barry', 'ChaLEes', 'Dao']
names2 = [name.lower() for name in names1]
print (names2[2][0])



numbers = [1, 2, 3, 4]
numbers.append("5,6,7,8")
print(len(numbers))






list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1
list3.append(6)
print(list1)
print(list1 + list2)
print(len(list1 + list2))






# def addItem(listParam):
#     listParam += 1
# mylist = [1, 2, 3, 4]
# addItem(mylist)
# print(len(mylist))




my_tuple = (1, 2, 3, 4)
my_tuple2 = (6, 2, 3, 4)
my_tuple = my_tuple + (2324,)
print(my_tuple[2])
print(my_tuple + my_tuple2)
print (len(my_tuple))
print (len(my_tuple + my_tuple2))

# my_tuple.append( (5, 6, 7) )
print("tupple")
print (len(my_tuple))



a = 1
b = 2
c = None
a,b,d = b,a,c
print(a,b,c,d)



def dostuff2(param1, *param2):
    print(type(param2))
dostuff2('apples', 'bananas', 'cherry', 'dates')



def dostuff(param1, **param2):
    print (type(param2))
dostuff('capitals', Arizona='Phoenix',
California='Sacramento', Texas='Austin')


# 
# counter = 1
# def doLotsOfStuff():
#     for i in (1, 2, 3):
#         counter += 1
# doLotsOfStuff()
# print(counter)


counter = 1
def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        
        counter += 1
        print(counter)
doLotsOfStuff()

print(counter)


# 
# dict2 = {"user","bill", "password":"abc","hillary"}
# print(dict2['password'])


name = "snow storm"
#name[5] = 'X'
print(name)

for i in range(2):
    print(i)
for i in range(4,6):
    print(i)


count = 0
while count < 10:
    print("Welcome to Python" ,count+1)
    count += 1



# x = "foo "
# y = 2
# print(x + y)

list3 =["a:1234554231","b:1234567890" ,"c:5432154321","d:9874563210","e:9874598745"]
same  = []
for li in list3 :
    print(li)
    vara = li[0][0]
    varb = li
    list4 = varb.split(":")
    variables2 = str(list4[1])
    len2 = len(variables2) // 2
    mid = variables2[0:len2]
    mid2 = variables2[len2:]
    
    sum1 = 0
    for m in mid :
        sum1 += int(m)
    print(sum)
    
    sum2 = 0
    for n in mid2 :
        sum2 += int(n)
    print(sum2)
    
    if sum1 == sum2 :
        same.append(vara)
