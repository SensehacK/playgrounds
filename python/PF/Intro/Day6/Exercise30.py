#PF-Exer-30

def find_average(mark_list):
    
    total=0
    try :
        for i in range(0, len(mark_list)):
            
        #for i in range(0, len(mark_list)):
            #total+=mark_list1[i]
            #total+=m_list[i]
            total+=mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    
    except NameError : 
        print("Except Name Error Block")
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except IndexError:
        print("Wrong IndexError data type")
        
    except : 
        print("Except Block")
    finally : 
        print("Finally Block")
        

#m_list=[]
try : 
    
    
#     mark1="A"
#     print(mark1) 
#     mark1=int("A")
#     print(mark1)  
#     m_list=[mark1,2,3,4]

   
    print("Hello Sensehack") 
except ValueError:
    print("Value error")
except NameError : 
    print("Except Name Error Block")
except ZeroDivisionError:
    print("Divide by Zero error")
except TypeError:
    print("Wrong data type")
    
except : 
    print("Except Block2")
finally : 
    print("Finally Block2")    
    
    
m_list=[1,2,3,4]
#m_list=["1",2,3,4]
try :
    
    print("m_list")
    print(m_list)
    print("Average marks:", find_average(m_list))
    
except NameError :
    print("End Name Error")
    
finally :
    print("Last finally")