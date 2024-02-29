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
        test_case = "...ant...ant..na..t.ant.t..ant...ant..ant..ant.anant..t" * 10000
        
        Time_start_new = time.time() #* 1000
        dead_ants_new(test_case)
        Time_stop_new = time.time() #* 1000

        Time_start_old = time.time() #* 1000
        dead_ants_count(test_case)
        Time_stop_old = time.time() #* 1000

        time_result_new = Time_stop_new - Time_start_new
        time_result_old = Time_stop_old - Time_start_old
        print("The time of ejecution in the new code is: ", time_result_new)
        print("The time of ejecution in the old code is: ", time_result_old)

        self.assertLess(time_result_new,time_result_old, msg="The old code is better than new code")
if __name__ == "__main__":
    unittest.main()
