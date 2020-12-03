import unittest
from unittest import mock
from unittest.mock import patch
from world.text import world
from io import StringIO
import sys
import robot
from world import obstacles


class test_world(unittest.TestCase):
    obst = [(125, 51), (-130, 62), (141, 136), (118, -38)]
    @mock.patch("world.obstacles.generate_obstacles", return_value=obst)
    def test_generate_obstacles(self, mock_randint):
        obst = [(125, 51), (-130, 62), (141, 136), (118, -38)]
        assert(obstacles.generate_obstacles() == obst)
    
    # def test_is_position_blocked(mock_randint):
    #     assert(obstacles.is_position_blocked(141, 136) == True)

    obst = [(-50, -146), (-107, -135), (-146, -235), (-113, 100), (-143, -191), (64, -51), (-105, 134), (31, -68), (118, -7), (-78, -135)]
    @mock.patch("world.obstacles.obstacles", obst)
    def test_generate_obstacles(self):
        assert(obstacles.is_position_blocked(30, -68) == True)
    

if __name__ == "__main__":
    unittest.main()