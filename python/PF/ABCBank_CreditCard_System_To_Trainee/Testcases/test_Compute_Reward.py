import pytest
from iTransact.Compute_Reward import calculate_reward_points,update_customer_reward_points

values=[('Gold',1000,{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },200),
        ('A',1000,{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },-1),
        ]
@pytest.mark.parametrize("card_type,transaction_amt, card_reward_details_dict, expected_value", values)
def test_calculate_reward_points(card_type,transaction_amt,card_reward_details_dict, expected_value):
    result=calculate_reward_points(card_type,transaction_amt,card_reward_details_dict)
    assert result==expected_value
    
values=[('1001','Gold',1000,{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },
                              {
                               '1001':['Gold','200'],
                               '1002':['Silver','20'],
                               '1009':['Business Gold','1200'],
                               '1004':['Titanium','2000'],
                               },
                               {
                               '1001':['Gold','400'],
                               '1002':['Silver','20'],
                               '1009':['Business Gold','1200'],
                               '1004':['Titanium','2000'],
                               }),
        ('1010','Gold',1000,{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },
                              {
                               '1001':['Gold','200'],
                               '1002':['Silver','20'],
                               '1009':['Business Gold','1200'],
                               '1004':['Titanium','2000'],
                               },
                               {
                               '1001':['Gold','200'],
                               '1002':['Silver','20'],
                               '1009':['Business Gold','1200'],
                               '1004':['Titanium','2000'],
                               '1010':['Gold','200'],
                               }),
        ('1001','Silver',1000,{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },
                              {
                               '1001':['Gold','200'],
                               '1002':['Silver','20'],
                               '1009':['Business Gold','1200'],
                               '1004':['Titanium','2000'],
                               },
                               -1),
        ('1001','ABC',1000,{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },
                              {
                               '1001':['Gold','200'],
                               '1002':['Silver','20'],
                               '1009':['Business Gold','1200'],
                               '1004':['Titanium','2000'],
                               },
                               -1),
        
        ]
@pytest.mark.parametrize("customer_id, card_type, transaction_amt,card_reward_details_dict,cust_reward_details_dict, expected_value", values)
def test_update_customer_reward_points(customer_id, card_type, transaction_amt,card_reward_details_dict,cust_reward_details_dict, expected_value):
    result=update_customer_reward_points(customer_id, card_type, transaction_amt,card_reward_details_dict,cust_reward_details_dict)
    assert result==expected_value