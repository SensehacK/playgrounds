'''
Created on Feb 15, 2017

@author: kautilya.save
'''

# 
# def fun(x,y):
#     if x==0:
#         return y 
#     else:
#         return fun(x-1,x+y)
#         print(x)
# print(fun(4,3))




# def fun(x,y):
#     if y==0:
#         return 0
#     return x+fun(x,y-1)
# 
# print(fun(2,4))




# 
# def fun(x,y):
#     if y==0:
#         return 0
#     return (x+fun(x,y-1))
# 
# def fun2(a,b):
#     if b==0:
#         return 1
#     return fun(a,fun2(a,b-1))
# 
# print(fun2(4,3)) 


# def fun(n):
#     if n<=0:
#         return
#     print(n%2,end='')
#     fun(n//2) 
# fun(25)

# def fun(n):
#     if n==4:
#         return n 
#     else:
#         return 2*fun(n+1) 
#      
# print(fun(2))

# what is the output of the following program?
# def fun(n):
#     if n==4:
#         return n 
#     else:
#         return 5+2*fun(n+1) 
#      
# print(fun(2))

# def fun(n,r):
#     if n>0:
#         return (n%r+fun(n//r,r))
#     else:
#         return 0
# print(fun(33, 2))


# 
# def fun(x,y):
#     if y==0:
#         return 0
#     return (x+fun(x,y-1))
# 
# def fun2(a,b):
#     if b==0:
#         return 1
#     return fun(a,fun2(a,b-1))
# 
# print(fun2(4,3))


# def fun(x,y):
#     if y==0:
#         return 1
#     else:
#         return x*fun(x,y-1)
# print(fun(4,3))
# 
# 
# 
# x = 4 
# y = 3
# print(x**y) # Power **


# def fun(x,y):
#     if y==0:
#         return x
#     else:
#         return fun(y,x%y)
# 
# print(fun(12,18))


# def fun(num):
#     if num==0 or num==1:
#         return num
#     return fun(num-1)+fun(num-2)
# print(fun(5))

# def fun(number,index):
#     if index==number:
#         return True
#     elif number%index==0:
#         return False
#     return fun(number, index+1)
# 
# print(fun(index=2,number=13))



#what is the output of the following program?

# def fun(n):
#     if n==0:
#         return 1
#     else:
#         return 2*fun(n-1)
# print(fun(5))

'''
a)32
b)64
c)16
d)runtime error




what is the output of the following program?

list2=[1,2,3,4,5]
def fun(list1):
    for list1[0] in list1:
        pass
    return list1
print(fun(list2))

'''


#what is the output of the following program?
# 
# x=[1,2,3,4,5,6,7]
# y=[6,7,8,9,10]
# z=x[-4:]+y[1:-1]
# print(z)


'''
what is the output of the following program?

def fun(n):
                if n==1:
                                return n
                else:
                                fun(n-1)
                                return n
print(fun(4))


#what is the output of the following program?

def fun(course):
                dict={"Btech":50000,"Mtech":125000,"MCA":45000,"BCA":30000}
                for key ,value in dict:
                                if key==course:
                                                return value
                                else:
                                                return -1

print(fun("Btech"))



'''

# what is the output of the following program?

# def fun(course):
#     dict={"Btech":50000,"Mtech":125000,"MCA":45000,"BCA":30000}
#     for key in dict:
#         print("key")
# 
# print(fun("Btech"))




'''
what is the output of the following program?

def fun(course):
                dict={"Btech":50000,"Mtech":125000,"MCA":45000,"BCA":30000}
                for key in dict:
                                print(key)

print(fun("Btech"))




what is the output of the following program?

def fun(x,y):
    try:
#         print(x[0])
#         print(type(x[0]))
#         print(type(y))
        if(x[0]//y==0):
            print(1)
        else:
            print(2)
        print(3)
    except ValueError:
        print(4)
    except IndexError:
        print(5)
    except ZeroDivisionError:
        print(6)
    except TypeError:
        print(10)
    
    finally:
        print(7)
    print(8)
fun("1234",0)
print(9)





what is the output of the following program?
'''
def fun(x,y):
    try:
        if(int(x[0])//y==0):
            print(1)
        else:
            print(2)
        print(3)
    
    except ValueError:
        print(4)
    except IndexError:
        print(5)
    except TypeError:
        print(10)
    except ZeroDivisionError:
        print(6)
    except:
        print("Some other error occurred")
    finally:
        print(7)
    print(8)
fun("1234",0)
print(9)

