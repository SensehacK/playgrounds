import pytest
from iCard.Update_Reward_Scheme import add_reward_scheme,update_reward_scheme

values=[('Gold','10','2',{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },-1),
        ('A','0','2',{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },-1),
        ('B','10','0',{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },-1),
        ('A','10','2',{
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              },
                              {
                              "Gold":['10','2'],
                              "Silver":['15','1'],
                              "Business Gold":['12','2'],
                              "Coral":['10','1'],
                              "A":['10','2']
                              })]
@pytest.mark.parametrize("card_type,min_transaction_amt, reward_point,card_reward_details_dict, expected_value", values)
def test_add_reward_scheme(card_type,min_transaction_amt, reward_point,card_reward_details_dict, expected_value):
    result=add_reward_scheme(card_type,min_transaction_amt, reward_point,card_reward_details_dict)
    assert result==expected_value

