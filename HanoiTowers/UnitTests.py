# - * - coding: utf-8 - * -

import unittest
import tkinter as tk 
from HanoiTowers import TowerOfHanoi

class TestTowerOfHanoi(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.num_disks = 4
        self.hanoi_game = TowerOfHanoi(self.root, self.num_disks)

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.hanoi_game.tower_a, [4, 3, 2, 1])
        self.assertEqual(self.hanoi_game.tower_b, [])
        self.assertEqual(self.hanoi_game.tower_c, [])

    def test_move_disk(self):
        self.hanoi_game.move_disk(self.hanoi_game.tower_a, self.hanoi_game.tower_b)
        self.assertEqual(self.hanoi_game.tower_a, [4, 3, 2])
        self.assertEqual(self.hanoi_game.tower_b, [1])

    def test_hanoi_algorithm(self):
        self.hanoi_game.hanoi(self.num_disks, self.hanoi_game.tower_a, self.hanoi_game.tower_c, self.hanoi_game.tower_b)
        self.assertEqual(self.hanoi_game.tower_a, [])
        self.assertEqual(self.hanoi_game.tower_b, [])
        self.assertEqual(self.hanoi_game.tower_c, [4, 3, 2, 1])

    def test_move_disks_half_full(self):
        self.hanoi_game.tower_a = [4, 3]
        self.hanoi_game.tower_b = [1]
        self.hanoi_game.move_disk(self.hanoi_game.tower_a, self.hanoi_game.tower_b)
        self.assertEqual(self.hanoi_game.tower_a, [4])
        self.assertEqual(self.hanoi_game.tower_b, [1, 3])

    def test_hanoi_algorithm_with_multiple_towers(self):
        self.hanoi_game.tower_a = [7, 6, 5, 4, 3, 2, 1]
        self.hanoi_game.tower_b = []
        self.hanoi_game.tower_c = []
        
        self.hanoi_game.hanoi(self.num_disks, self.hanoi_game.tower_a, self.hanoi_game.tower_c, self.hanoi_game.tower_b)
        
        self.assertEqual(self.hanoi_game.tower_a, [7, 6, 5])
        self.assertEqual(self.hanoi_game.tower_b, [])
        self.assertEqual(self.hanoi_game.tower_c, [4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()

