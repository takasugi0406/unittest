import unittest
from calculate_reward import *

import unittest

class TestCalculateReward(unittest.TestCase):
    def test_R1_no_reward(self):
        # Không nhận được phần thưởng
        role = "người chơi thường"
        point = 8
        self.assertEqual(calculate_reward(role, point), 0)
    
    def test_R2_no_reward(self):
        # Không nhận được phần thưởng
        role = "người chơi thường"
        point = 55
        self.assertEqual(calculate_reward(role, point), 0)

    def test_R3_no_reward(self):
        # Không nhận được phần thưởng
        role = "người chơi thường"
        point = 600
        self.assertEqual(calculate_reward(role, point), 0)

    def test_R4_reward_1000_coins(self):
        # Nhận được phần thưởng là 1000 coins
        role = "người chơi thường"
        point = 1500
        self.assertEqual(calculate_reward(role, point), 1000)
    
    def test_R5_no_reward(self):
        # Không nhận được phần thưởng
        role = "vip1"
        point = 6
        self.assertEqual(calculate_reward(role, point), 0)

    def test_R6_no_reward(self):
        # Không nhận được phần thưởng
        role = "vip1"
        point = 80
        self.assertEqual(calculate_reward(role, point), 0)

    def test_R7_reward_1000_coins(self):
        # Nhận được phần thưởng là 1000 coins
        role = "vip1"
        point = 999
        self.assertEqual(calculate_reward(role, point), 1000)

    
    def test_R8_reward_5000_coins(self):
        # Nhận được phần thưởng là 5000 coins
        role = "vip1"
        point = 1000
        self.assertEqual(calculate_reward(role, point), 5000)
    
    def test_R9_reward_1000_coins(self):
        # Nhận được phần thưởng là 1000 coins
        role = "vip2"
        point = 0
        self.assertEqual(calculate_reward(role, point), 1000)
    
    def test_R10_reward_5000_coins(self):
        # Nhận được phần thưởng là 5000 coins
        role = "vip2"
        point = 12
        self.assertEqual(calculate_reward(role, point), 5000)
    
    def test_R11_reward_10000_coins(self):
        # Nhận được phần thưởng là 10000 coins
        role = "vip2"
        point = 500
        self.assertEqual(calculate_reward(role, point), 10000)

    def test_R5_reward_50000_coins(self):
        # Nhận được phần thưởng là 50000 coins
        role = "vip2"
        point = 1500
        self.assertEqual(calculate_reward(role, point), 50000)

if __name__ == '__main__':
    unittest.main()
