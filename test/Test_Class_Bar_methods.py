__author__ = 'Tom'
import unittest
import Class_Bar


class Positional_Attributes(unittest.TestCase):
      def setUp(self):
          bar = Class_Bar.Bar(80, 30, 50, 300)
          #Y_Diff = abs(bar.top_y_boundary() - bar.bottom_y_boundary())

      def tearDown(self):
          self.widget.dispose()
          self.widget = None

      def test_y_boundary_bottom(self):
          self.assertEqual()