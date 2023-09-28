import unittest
from calculate_reward import *

import unittest

class TestCalculateReward(unittest.TestCase):
    def test_OE1_no_reward(self):
        # Không nhận được phần thưởng
        role = "người chơi thường"
        point = 90
        self.assertEqual(calculate_reward(role, point), 0)

    def test_OE2_reward_1000_coins(self):
        # Nhận được phần thưởng là 1000 coins
        role = "vip2"
        point = 8
        self.assertEqual(calculate_reward(role, point), 1000)

    def test_OE3_reward_5000_coins(self):
        # Nhận được phần thưởng là 5000 coins
        role = "vip1"
        point = 1020
        self.assertEqual(calculate_reward(role, point), 5000)

    def test_OE4_reward_10000_coins(self):
        # Nhận được phần thưởng là 10000 coins
        role = "vip2"
        point = 150
        self.assertEqual(calculate_reward(role, point), 10000)

    def test_OE5_reward_50000_coins(self):
        # Nhận được phần thưởng là 50000 coins
        role = "vip2"
        point = 1010
        self.assertEqual(calculate_reward(role, point), 50000)

if __name__ == '__main__':
    unittest.main()
