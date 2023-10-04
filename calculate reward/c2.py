import unittest
from calculate_reward import *

import unittest

class TestCalculateReward(unittest.TestCase):
    def test_TC1(self):
        role = "người chơi thường"
        point = 1001
        self.assertEqual(calculate_reward(role, point), 1000)
    
    def test_TC2(self):
        role = "người chơi thường"
        point = 300
        self.assertEqual(calculate_reward(role, point), 0)

    def test_TC3(self):
        role = "vip1"
        point = 800
        self.assertEqual(calculate_reward(role, point), 1000)
    
    def test_TC4(self):
        role = "vip1"
        point = 1200
        self.assertEqual(calculate_reward(role, point), 5000)

    def test_TC5(self):
        role = "vip1"
        point = 80
        self.assertEqual(calculate_reward(role, point), 0)

    def test_TC6(self):
        role = "vip2"
        point = 3
        self.assertEqual(calculate_reward(role, point), 1000)

    
    def test_TC7(self):
        role = "vip2"
        point = 13
        self.assertEqual(calculate_reward(role, point), 5000)
    
    def test_TC8(self):
        role = "vip2"
        point = 450
        self.assertEqual(calculate_reward(role, point), 10000)
    
    def test_TC9(self):
        role = "vip2"
        point = 1322
        self.assertEqual(calculate_reward(role, point), 50000)
    
    def test_TC10(self):
        role = "vip2"
        point = -1
        self.assertEqual(calculate_reward(role, point), 0)

    def test_TC11(self):
        role = None
        point = 0
        self.assertEqual(calculate_reward(role, point), 0)

if __name__ == '__main__':
    unittest.main()
