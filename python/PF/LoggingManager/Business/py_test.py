'''
Created on Nov 22, 2016

@author: Abhilash.S12
'''

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Business.BuisnessModule import validate_emailid,validate_pan,validate_phone


   
def test_validate_phone():
    invalid_phone='154we78er2'
    expected_output=False
    actual_output=validate_phone(invalid_phone)
    assert actual_output==expected_output

def test_validate_phone_1():
    valid_phone='7894561232'
    expected_output=True
    actual_output=validate_phone(valid_phone)
    assert actual_output==expected_output
    
def test_validate_phone_2():
    invalid_phone='78945613303'
    expected_output=False
    actual_output=validate_phone(invalid_phone)
    assert actual_output==expected_output
    
def test_validate_phone_3():
    invalid_phone='78945613'
    expected_output=False
    actual_output=validate_phone(invalid_phone)
    assert actual_output==expected_output

    
def test_validate_pan():
    invalid_pan='DASDER4444A'
    expected_output=False
    actual_output=validate_pan(invalid_pan)
    assert actual_output==expected_output

def test_validate_pan_1():
    valid_pan='ASDER4444A'
    expected_output=True
    actual_output=validate_pan(valid_pan)
    assert actual_output==expected_output
    
def test_validate_pan_2():
    invalid_pan='ASDER4444AD'
    expected_output=False
    actual_output=validate_pan(invalid_pan)
    assert actual_output==expected_output
    
def test_validate_pan_3():
    invalid_pan='ASDE4444AD'
    expected_output=False
    actual_output=validate_pan(invalid_pan)
    assert actual_output==expected_output

def test_validate_pan_4():
    invalid_pan='ASDER444AD'
    expected_output=False
    actual_output=validate_pan(invalid_pan)
    assert actual_output==expected_output
    
def test_validate_pan_5():
    invalid_pan='ASDE4444'
    expected_output=False
    actual_output=validate_pan(invalid_pan)
    assert actual_output==expected_output
    
def test_validate_email():
    valid_email='abc@d.com'
    expected_output=True
    actual_output=validate_emailid(valid_email)
    assert actual_output==expected_output
    
def test_validate_email_1():
    valid_email='ab_c@d.co.in'
    expected_output=True
    actual_output=validate_emailid(valid_email)
    assert actual_output==expected_output

def test_validate_email_2():
    invalid_email='a.b_c@d.co.bi.er'
    expected_output=False
    actual_output=validate_emailid(invalid_email)
    assert actual_output==expected_output
    
def test_validate_email_3():
    invalid_email='a.c_b@d.co.us'
    expected_output=False
    actual_output=validate_emailid(invalid_email)
    assert actual_output==expected_output

def test_validate_email_4():
    invalid_email='a_@b.co.us'
    expected_output=False
    actual_output=validate_emailid(invalid_email)
    assert actual_output==expected_output
