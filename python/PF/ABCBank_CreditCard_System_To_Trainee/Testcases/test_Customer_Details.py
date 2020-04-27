import pytest
from iTransact.Customer_Details import get_top_customer

values=[({
                              "1200":['Gold','20'],
                              "1210":['Silver','10'],
                              "1111":['Platinum','02'],
                              "1001":['Business','100'],
                              },'1001'),
        
        
       ]
@pytest.mark.parametrize("cust_reward_details_dict, expected_value", values)
def test_get_top_customer(cust_reward_details_dict, expected_value):
    result=get_top_customer(cust_reward_details_dict)
    assert result==expected_value
    