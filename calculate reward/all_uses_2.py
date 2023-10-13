import unittest
from calculate_reward_2 import *

import unittest

class TestCalculateReward(unittest.TestCase):
    def test_TC1(self):
        role = "người chơi thường"
        point = 1001
        self.assertEqual(calculate_reward_2(role, point), 1000)
    
    def test_TC2(self):
        role = "vip1"
        point = 500
        self.assertEqual(calculate_reward_2(role, point), 1000)

    def test_TC3(self):
        role = "vip1"
        point = 800
        self.assertEqual(calculate_reward_2(role, point), 1000)
    
    def test_TC4(self):
        role = None
        point = 0
        self.assertEqual(calculate_reward_2(role, point), 0)

    def test_TC5(self):
        role = "vip2"
        point = 5
        self.assertEqual(calculate_reward_2(role, point), 1000)

    def test_TC6(self):
        role = None
        point = 0
        self.assertEqual(calculate_reward_2(role, point), 0)
    


    def test_TC7(self):
        role = "người chơi thường"
        point = 1023
        self.assertEqual(calculate_reward_2(role, point), 1000)
    
    def test_TC8(self):
        role = "người chơi thường"
        point = 499
        self.assertEqual(calculate_reward_2(role, point), 0)
    
    def test_TC9(self):
        role = "vip1"
        point = 500
        self.assertEqual(calculate_reward_2(role, point), 1000)
    
    def test_TC10(self):
        role = "vip1"
        point = 1500
        self.assertEqual(calculate_reward_2(role, point), 5000)
    
    def test_TC11(self):
        role = "vip1"
        point = 1500
        self.assertEqual(calculate_reward_2(role, point), 5000)

    def test_TC12(self):
        role = "vip1"
        point = 33
        self.assertEqual(calculate_reward_2(role, point), 0)

    def test_TC13(self):
        role = "vip2"
        point = 3
        self.assertEqual(calculate_reward_2(role, point), 1000)
    
    def test_TC14(self):
        role = "vip2"
        point = 13
        self.assertEqual(calculate_reward_2(role, point), 5000)
    
    def test_TC15(self):
        role = "vip2"
        point = 14
        self.assertEqual(calculate_reward_2(role, point), 5000)
    
    def test_TC16(self):
        role = "vip2"
        point = 144
        self.assertEqual(calculate_reward_2(role, point), 10000)
    
    def test_TC17(self):
        role = "vip2"
        point = 999
        self.assertEqual(calculate_reward_2(role, point), 10000)
    
    def test_TC18(self):
        role = "vip2"
        point = 1331
        self.assertEqual(calculate_reward_2(role, point), 50000)
    
    def test_TC19(self):
        role = "vip2"
        point = 5555
        self.assertEqual(calculate_reward_2(role, point), 50000)
    
    def test_TC20(self):
        role = "vip2"
        point = -1
        self.assertEqual(calculate_reward_2(role, point), 0)

if __name__ == '__main__':
    unittest.main()
