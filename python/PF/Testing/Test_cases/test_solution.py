#PF-TCV-Exer-20

import pytest
from Test_cases.solution import boarding

def test_boarding_1():
        result=boarding(3)
        assert result==1
                
def test_boarding_2():
        result=boarding(24)
        assert result==1
        
def test_boarding_3():
        result=boarding(75)
        assert result==2

def test_boarding_4():
        result=boarding(104)
        assert result==3
             

def test_boarding_5():
        result=boarding(255)
        assert result==-1
             