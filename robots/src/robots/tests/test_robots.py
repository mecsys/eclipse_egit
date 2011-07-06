#!/usr/bin/env python
import unittest
class Test(unittest.TestCase):   
    
    def get_expected_pos(self):
        return 2, 1

    def test_robots(self):
        from robots.core import Robot
        robot = Robot(x=0, y=0)
        robot.print_mood()  
        robot.walk(x=2, y=1)
        expected_position = self.get_expected_pos()
        self.assertEqual(robot.get_pos(), expected_position)
        robot.print_mood()  
        robot.walk(x=2, y=1)
        robot.print_mood()