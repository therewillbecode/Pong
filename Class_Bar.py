__author__ = 'Tom'
import pygame
__doc__ ="""
"""


#   class for paddle bar used to hit ball
class Bar:
    cnt = 0 # cnt would be shared by all instances of the class 

    def __init__(self, length, width, start_x, start_y):
        self.x_pos_center = start_x
        self.y_pos_center = start_y
        self.length = length
        self.width = width
        self.__class_.cnt+=1

    def draw(self, gameDisplay, color):
        pygame.draw.rect(gameDisplay, color, [self.x_pos_center, self.y_pos_center, self.width, self.length])
        

    @classmethod
    def getCount(cls):
        return cls.cnt
    #Bar.getCount()

    @staticmethod
    def example():
        return 1+2
    # Math.sqrt()

    def right_edge_x_boundary(self):
        return self.x_pos_center + (0.5 * self.width)

    def left_x_boundary(self):
        return self.x_pos_center - (0.5 * self.width)

    def top_y_boundary(self):
        return pygame.mouse.get_pos()[1] - (0.5 * self.length)

    def bottom_y_boundary(self):
        return pygame.mouse.get_pos()[1] + (0.5 * self.length)
