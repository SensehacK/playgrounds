'''
Created on Mar 10, 2017

@author: kautilya.save
'''
from memory_profiler import profile
@profile
def datasize() :
    str_input = "20KB"

    input_size = str_input[-2:]
    output_str = ''
    
    if input_size == "TB"  :
        output_str = str(int(str_input[:-2]) * 1000)
        output_str += "GB"
    elif  input_size == "GB"  :
        output_str = str(int(str_input[:-2]) * 1000)
        output_str += "MB"
    elif  input_size == "PB"  :
        output_str = str(int(str_input[:-2]) * 1000)
        output_str += "TB"
    elif  input_size == "MB"  :
        output_str = str(int(str_input[:-2]) * 1000)
        output_str += "KB"
    elif  input_size == "KB"  :
        output_str = str(int(str_input[:-2]) * 1000)
        output_str += "B"    
    print(output_str)
    
datasize()