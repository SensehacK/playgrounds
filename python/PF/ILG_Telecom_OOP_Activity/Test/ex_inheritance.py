
import unittest
from DataAccess.bean import DTH,Broadband,VoIP,Product


''' To test inheritance Implementation '''

class Mytestcase(unittest.TestCase):
   
    
    def test_dth(self):
        flag=1
        dth=DTH("D1001", "", 500, "TiVo", "Silver")
        self.assertIsInstance(dth,Product,'DTH class has not been Inherited')
        try:
            self.assertIsNotNone(dth.get_prod_id(), 'No Super call')
        except:
            flag = 0     
        if(flag == 0):
            self.assertTrue(False,'No super call')
    def test_voip(self):
        flag=1
        voip=VoIP("V1001", "prod_name", 500, "Skype", 450, 120)
        self.assertIsInstance(voip,Product,'VoIP class has not been Inherited')
        try:
            self.assertIsNotNone(voip.get_prod_id(), 'No Super call')
        except:
            flag = 0
        if(flag == 0):
            self.assertTrue(False,'No super call')
    def test_broadband(self):
        flag=1
        broadband=Broadband("B1001", "prod_name", 1200, 5, 40)
        self.assertIsInstance(broadband,Product,'Broadband class has not been Inherited') 
        try:
            self.assertIsNotNone(broadband.get_prod_id(), 'No Super call')
        except:
            flag = 0   
        if(flag == 0):
            self.assertTrue(False,'No super call')
    
         

if __name__ == '__main__':
    unittest.main()