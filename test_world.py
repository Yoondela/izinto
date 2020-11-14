import unittest
from unittest.mock import patch
from world.text import world
from io import StringIO
import sys
import robot

class test_world(unittest.TestCase):
    @patch("sys.stdin", StringIO("Bob\nforward 5\noff"))
    def test_show_position(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            val = the_output.getvalue()
            self.assertEqual(val,"""What do you want to name your robot? Bob: Hello kiddo!
Bob: What must I do next?  > Bob moved forward by 5 steps.
 > Bob now at position (0,5).
Bob: What must I do next? Bob: Shutting down..
""")


    @patch("sys.stdin", StringIO("Bob\nforward 10\noff"))
    def test_update_position(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            val = the_output.getvalue()
            self.assertEqual(val,"""What do you want to name your robot? Bob: Hello kiddo!
Bob: What must I do next?  > Bob moved forward by 10 steps.
 > Bob now at position (0,10).
Bob: What must I do next? Bob: Shutting down..
""")


    @patch("sys.stdin", StringIO("Bob\nforward 201\noff"))
    def test_is_position_allowed_forward(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            val = the_output.getvalue()
            self.assertEqual(val,"""What do you want to name your robot? Bob: Hello kiddo!
Bob: What must I do next? Bob: Sorry, I cannot go outside my safe zone.
 > Bob now at position (0,0).
Bob: What must I do next? Bob: Shutting down..
""")


    @patch("sys.stdin", StringIO("Bob\nback 201\noff"))
    def test_is_position_allowed_back(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            val = the_output.getvalue()
            self.assertEqual(val,"""What do you want to name your robot? Bob: Hello kiddo!
Bob: What must I do next? Bob: Sorry, I cannot go outside my safe zone.
 > Bob now at position (0,0).
Bob: What must I do next? Bob: Shutting down..
""")




if __name__ == "__main__":
    unittest.main()