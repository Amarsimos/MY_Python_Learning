#from 11-1-city_fun import city_fun  不能数字开头,不能用-号
from Employee import Employee
import unittest 
 
class EmployeeTestCase(unittest.TestCase): 
     
    def setUp(self): 
        self.gen = Employee("Gen","Smith",50000) 
        
    def test_give_default_raise(self): 
        self.gen.give_raise() 
        default_salary = self.gen.salary 
        self.assertEqual(default_salary,55000) 
 
    def test_give_custom_raise(self): 
        self.gen.give_raise(10000) 
        custom_salary = self.gen.salary 
        self.assertEqual(custom_salary,60000) 
unittest.main()