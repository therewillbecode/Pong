__author__ = 'Tom'
import pygame
import index
__doc__ ="""
"""


#   class for paddle bar used to hit ball
class Bar:

    def __init__(self, length, width, start_x, start_y):
        self.x_pos_center = start_x
        self.y_pos_center = start_y
        self.length = length
        self.width = width
        pygame.draw.rect(index.gameDisplay, index.white, [start_x, start_y, width, length])

    @classmethod
    def right_edge_x_boundary(self):
        return self.x_pos_center + (0.5 * self.width)

    @classmethod
    def left_x_boundary(self):
        return self.x_pos_center - (0.5 * self.width)

    @classmethod
    def top_y_boundary(self):
        return self.y_pos_center - (0.5 * self.length)

    @classmethod
    def bottom_y_boundary(self):
        return self.y_pos_center + (0.5 * self.length)
