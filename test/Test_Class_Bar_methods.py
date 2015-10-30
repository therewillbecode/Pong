__author__ = 'Tom'
__doc__ = """ test class methods for Bar """
import unittest
import Class_Bar


class Positional_Attributes(unittest.TestCase):
      def setUp(self):  # having issues setting up mock
          bar = Class_Bar.Bar(80, 30, 50, 300)
          Y_Diff = abs(bar.top_y_boundary() - bar.bottom_y_boundary())   # difference between y coordinates of top and bottom edges of bar

      def tearDown(self):
          self.widget.dispose()
          self.widget = None

      def test_y_boundary_bottom(self):
          self.assertEqual()    # checks that bar is