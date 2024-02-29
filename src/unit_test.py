import unittest, time
from old_algoritm_dead_ants import dead_ants_count
from new_algoritm_dead_ants import dead_ants_new

class TestCountDeadAnts(unittest.TestCase):

    def test_case_1(self):
        test_case = "...ant...ant..na..t.ant.t..ant...ant..ant..ant.anant..t"
        self.assertEqual(dead_ants_new(test_case), 3)
        self.assertEqual(dead_ants_count(test_case), 3)
        
        
    def test_case_2(self):
        test_case = " "
        self.assertEqual(dead_ants_new(test_case),0)
        self.assertEqual(dead_ants_count(test_case), 0)
    
    def test_case_3(self):
        test_case = "ant nat ant t ant"
        self.assertEqual(dead_ants_new(test_case),2)
        self.assertEqual(dead_ants_count(test_case), 2)
        
    def test_case_4(self):
        test_case = "ant #@nat #@ant t#@? ant#!@"
        self.assertEqual(dead_ants_count(test_case),2)
        self.assertEqual(dead_ants_count(test_case), 2)
    
    def test_case_5(self):
        test_case = "ant12332nat343ant4343t4342ant"
        self.assertEqual(dead_ants_new(test_case),2)
        self.assertEqual(dead_ants_count(test_case), 2)
    
    def test_case_6(self):
        test_case = "123456789"
        self.assertEqual(dead_ants_new(test_case),0)
        self.assertEqual(dead_ants_count(test_case), 0)
    
    def test_case_7(self):
        test_case = "xyz"
        self.assertEqual(dead_ants_new(test_case),0)
        self.assertEqual(dead_ants_count(test_case), 0)
    
    def test_case_8(self):
        test_case = "...ant...ant..na..t.ant.t..ant...ant..ant..ant.anant..t"
        Time_new = self.assertEqual(dead_ants_new(test_case),3)
        Time_old = self.assertEqual(dead_ants_count(test_case), 3)
    

if __name__ == "__main__":
    unittest.main()