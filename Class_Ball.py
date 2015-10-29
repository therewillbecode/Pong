import pygame
import index


class Ball:

    def __init__(self, start_x, start_y, colour, radius):
        self.x_pos = start_x
        self.y_pos = start_y
        self.colour = colour
        self.radius = radius
        self.x_change = -2
        self.y_change = -2
        pygame.draw.circle(index.gameDisplay, self.colour, [start_x, start_y], radius)

    def update_pos(self):
        self.is_boundary_collision()         # change direction if boundary is hit
        self.traverse()                      # move in direction

    def traverse(self):
        self.x_pos += self.x_change
        self.y_pos += self.y_change
    #   print("self.y_pos" + str(self.y_pos))

    def is_boundary_collision(self):
        # window boundaries
        if self.x_pos < 0 + self.radius or self.x_pos > index.window_width - self.radius:
            self.change_direction_x()
        if self.y_pos < 0 + self.radius or self.y_pos > index.window_height - self.radius:
            self.change_direction_y()

        # bar_boundary_x - circle hits side of bar
        if index.lead_y < self.y_pos < index.lead_y + index.bar_length:
            if index.lead_x > self.x_pos - self.radius:
                self.change_direction_x()

        # bar_boundary_y - circle hits top or bottom of bar
        if index.lead_y - index.bar_length < self.y_pos - self.radius < index.lead_y + index.bar_length:
            if index.lead_x - index.bar_width > self.x_pos - self.radius < index.lead_x + index.bar_width:
                self.change_direction_y()

    def change_direction_x(self):
        self.x_change *= -1

    def change_direction_y(self):
        self.y_change *= -1