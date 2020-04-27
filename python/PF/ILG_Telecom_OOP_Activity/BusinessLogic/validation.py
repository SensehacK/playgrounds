
from DataAccess.DAO import CustomerDAO


class Validator:
    # Method to validate customer id and password
    @staticmethod
    def login_check(customer_id,password):
        flag = False                                                # flag to capture Invalid Customer ID
        customer_list = CustomerDAO.get_customer_details()          # fetch customer list
        for customer_obj in customer_list:                          # Iterating through customer objects
            if(customer_obj.get_customer_id()== customer_id):       # check if customer id matches
                flag = True                                         # Reset flag if Customer Id is found
                if(customer_obj.get_password()!=password):          # check if password matches
                    raise Exception("Password Mismatch")            # raise exception on invalid input
                else:
                    customer_dao=CustomerDAO(customer_obj)          # create customer DAO object on valid credentials
                    return customer_dao
        if(flag==False):
            raise Exception("Invalid Customer")                     # raise exception on invalid input