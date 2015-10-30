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
    def right_edge_x_boundary(cls, bar):
        return bar.x_pos_center + (0.5 * bar.width)

    @classmethod
    def left_x_boundary(cls, bar):
        return bar.x_pos_center - (0.5 * bar.width)

    @classmethod
    def top_y_boundary(cls, bar):
        return pygame.mouse.get_pos()[1] - (0.5 * bar.length)

    @classmethod
    def bottom_y_boundary(cls, bar):
        return pygame.mouse.get_pos()[1] + (0.5 * bar.length)
