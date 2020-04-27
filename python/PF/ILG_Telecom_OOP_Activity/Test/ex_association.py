import unittest
from DataAccess.bean import Customer
from DataAccess.DAO import CustomerDAO


''' To test association implementation '''

class Exercise5TestCases(unittest.TestCase):

    def test_purchase_deal1(self):        
        current_customer = Customer()
        current_customer.set_subscription_amount(0)
        
        cust_dao = CustomerDAO(current_customer)        
        
        cust_dao.purchase_deal("DEAL-001")
        self.assertEqual(1450, current_customer.get_subscription_amount(), "Error in Subscription amount calculation")
        
    def test_purchase_deal2(self):        
        current_customer = Customer()
        current_customer.set_subscription_amount(500)
        
        cust_dao = CustomerDAO(current_customer)        
        
        cust_dao.purchase_deal("deal-002")
        self.assertEqual(1900, current_customer.get_subscription_amount(), "Error in Subscription amount calculation")
    
    def test_purchase_deal3(self):        
        current_customer = Customer()
        current_customer.set_subscription_amount(0)
        
        cust_dao = CustomerDAO(current_customer)      
        required_list_of_products = [cust_dao.product_list[0], cust_dao.product_list[1]]  
        
        cust_dao.purchase_deal("DEAL-001")
        self.assertEqual(len(required_list_of_products), len(current_customer.get_product_list()), "Error in updating Product list of current customer")
        self.assertEqual(required_list_of_products[0].__dict__, current_customer.get_product_list()[0].__dict__, "Error in updating Product list of current customer")
        self.assertEqual(required_list_of_products[1].__dict__, current_customer.get_product_list()[1].__dict__, "Error in updating Product list of current customer")
    
    def test_purchase_deal4(self):        
        current_customer = Customer()
        cust_dao = CustomerDAO(current_customer)
        
        current_customer.set_subscription_amount(500)
        current_customer.set_product_list([cust_dao.product_list[0]])
                      
        required_list_of_products = [cust_dao.product_list[0], cust_dao.product_list[1], cust_dao.product_list[2]]  
        
        cust_dao.purchase_deal("Deal-002")
        self.assertEqual(len(required_list_of_products), len(current_customer.get_product_list()), "Error in updating Product list of current customer")
        self.assertEqual(required_list_of_products[0].__dict__, current_customer.get_product_list()[0].__dict__, "Error in updating Product list of current customer")
        self.assertEqual(required_list_of_products[1].__dict__, current_customer.get_product_list()[1].__dict__, "Error in updating Product list of current customer")
        self.assertEqual(required_list_of_products[2].__dict__, current_customer.get_product_list()[2].__dict__, "Error in updating Product list of current customer")

    
if __name__ == '__main__':
    unittest.main()