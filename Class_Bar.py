__author__ = 'Tom'
import pygame
__doc__ = """
"""

#   class for paddle bar used to hit ball
class Bar:
    cnt = 0  # cnt would be shared by all instances of the class
    x_pos = 0   # x coordinate of centre of bar
  #  y_pos = pygame.mouse.get_pos()[1]    # y coordinate of centre of bar

    def __init__(self, length, width, start_x, start_y):
        self.x_pos = start_x
        self.y_pos = 0
        self.length = length
        self.width = width
        self.__class__.cnt += 1

    def draw(self, gameDisplay, color):
        pygame.draw.rect(gameDisplay, color, [self.x_pos, self.y_pos, self.width, self.length])

    @classmethod
    def getCount(cls):
        return cls.cnt
    #Bar.getCount()

    def right_edge_x_boundary(self):
        return self.x_pos + (0.5 * self.width)

    def left_x_boundary(self):
        return self.x_pos - (0.5 * self.width)

    def top_y_boundary(self):
        return self.y_pos - (0.5 * self.length)

    def bottom_y_boundary(self):
        return self.y_pos + (0.5 * self.length)
