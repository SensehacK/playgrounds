def calculate_sum(list_of_expenditure):
    total=0
    no_values = []
    try:
        for expenditure in list_of_expenditure:
            raise Excelp()
            total+=expenditure
        print("Total:",total)
        avg=total/no_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        
        print("Wrong data type")
    except NameError:
        print("Name error occured22")
        
    except Excelp :
        print("Hello")

try:
    list_of_values=[100,200,300,400,500]
    num_values=len(list_of_values)
    calculate_sum(list_of_values)
except NameError:
    print("Name error occured2")
except:
    print("Some error occured")

class Excelp (Exception):
    def __init__(self):
        message = "Excelp is the exception"
        
        super().__init__(message)        
