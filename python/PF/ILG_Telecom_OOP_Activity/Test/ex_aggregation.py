
import unittest

from DataAccess.bean import Address, Customer
from DataAccess.DAO import CustomerDAO


''' To test aggregation implementation '''

class Exercise4TestCases(unittest.TestCase):   
    def __init__(self, method_name):
        super().__init__(method_name)
        current_comm_address = Address("Comm Line 1", "Comm Line 2", "Comm city", "Comm state", 123456)
        current_inst_address = Address("Inst Line 1", "Inst Line 2", "Inst city", "Inst state", 123456)
        current_customer = Customer()
        current_customer.set_communication_address(current_comm_address)
        current_customer.set_installation_address(current_inst_address)
        
        self.cust_dao = CustomerDAO(current_customer)
        
    
    def test_update_communication_address(self):        
        new_comm_address = Address("New Comm Line 1", "New Comm Line 2", "New Comm city", "New Comm state", 112233)
        
        self.cust_dao.update_communication_address(new_comm_address)
        self.assertEqual(new_comm_address, self.cust_dao.get_current_customer().get_communication_address(), "update_communication_address method is not implemented correctly")
        
        
    def test_update_installation_address(self):
        new_inst_address = Address("New Inst Line 1", "New Inst Line 2", "New Inst city", "New Inst state", 111222)
        
        self.cust_dao.update_installation_address(new_inst_address)
        self.assertEqual(new_inst_address, self.cust_dao.get_current_customer().get_installation_address(), "update_installation_address method is not implemented correctly")
   

if __name__ == '__main__':
    unittest.main()