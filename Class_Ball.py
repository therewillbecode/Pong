import pygame
from index import *

class Ball:

    def __init__(self, start_x, start_y, colour, radius):
        self.x_pos = start_x
        self.y_pos = start_y
        self.colour = colour
        self.radius = radius
        self.x_change = -2
        self.y_change = -2
        pygame.draw.circle(gameDisplay, colour, [start_x, start_y], radius)

    def update_pos(self):
        self.is_boundary_collision()         # change direction if boundary is hit
        self.traverse()                      # move in direction

    def traverse(self):
        self.x_pos += self.x_change
        self.y_pos += self.y_change
    #   print("self.y_pos" + str(self.y_pos))

    def is_boundary_collision(self):
        # window boundaries
        if self.x_pos < 0 + self.radius or self.x_pos > window_width - self.radius:
            self.change_direction_x()
        if self.y_pos < 0 + self.radius or self.y_pos > window_height - self.radius:
            self.change_direction_y()

        # bar_boundary_x - circle hits side of bar
        if lead_y < self.y_pos < lead_y + bar_length:
            if lead_x > self.x_pos - self.radius:
                print('f')
                self.change_direction_x()

        # bar_boundary_y - circle hits top or bottom of bar
        if lead_y < self.y_pos < lead_y + bar_length:
            if lead_x > self.x_pos - self.radius:
                print('g')
                self.change_direction_y()

    def change_direction_x(self):
        self.x_change *= -1

    def change_direction_y(self):
        self.y_change *= -1

