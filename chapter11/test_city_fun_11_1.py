#from 11-1-city_fun import city_fun  不能数字开头,不能用-号
from city_fun_11_1 import city_funs
import unittest 
 
class CityTestCase(unittest.TestCase): 
    """测试city_fun.py""" 
     
    def test_city_fun(self): 
        """能够正确地处理像New York这样的城市名吗?""" 
        formatted_city = city_funs('new york','usa') 
        self.assertEqual(formatted_city, 'new york,usa') 
 
unittest.main()