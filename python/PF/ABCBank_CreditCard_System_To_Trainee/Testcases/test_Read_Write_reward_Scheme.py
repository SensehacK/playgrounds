import pytest
from iCard.Read_Write_Reward_Scheme import create_dict_from_lists

values=[(['Gold','Silver','Platinum', 'Business'],['12','10','5','5'],['2','3','1','3'],{
                              "Gold":['12','2'],
                              "Silver":['10','3'],
                              "Platinum":['5','1'],
                              "Business":['5','3'],
                              }),
        
       ]
@pytest.mark.parametrize("card_type_list,min_trasaction_amt_list,reward_point_list, expected_value", values)
def test_create_dict_from_lists(card_type_list,min_trasaction_amt_list,reward_point_list, expected_value):
    result=create_dict_from_lists(card_type_list,min_trasaction_amt_list,reward_point_list)
    assert result==expected_value