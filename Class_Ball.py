import pygame
import index



class Ball:
    x_pos = 0   # x coordinate of centre of ball
    y_pos = 0   # y coordinate of centre of ball
    SPEEDX = 2
    SPEEDY = 2

    def __init__(self, start_x, start_y, colour, radius):
        self.x_pos = start_x
        self.y_pos = start_y
        self.colour = colour
        self.radius = radius
        self.x_change = self.SPEEDX
        self.y_change = self.SPEEDY

    def draw(self, gameDisplay):
        pygame.draw.circle(gameDisplay, self.colour, [self.x_pos, self.y_pos], self.radius)

    def update_pos(self, bar_list):
        self.update_on_collision(bar_list)         # change direction if boundary is hit
        self.traverse()                      # move in direction

    def traverse(self):
        self.x_pos += self.x_change
        self.y_pos += self.y_change
    #   print("self.y_pos" + str(self.y_pos))

    def update_on_collision(self, bar_list):
        self.handle_window_boundary()
        print(bar_list[0].left_x_boundary())
        print(bar_list[0].right_edge_x_boundary())
        # change to loop for all bars
        self.handle_bar_boundary_x(bar_list[0])
        self.handle_bar_boundary_y(bar_list[0])

    def handle_window_boundary(self):  # window boundaries
        if self.x_pos < 0 + self.radius or self.x_pos > index.window_width - self.radius:
            self.change_direction_x()
        if self.y_pos < 0 + self.radius or self.y_pos > index.window_height - self.radius:
            self.change_direction_y()

    def handle_bar_boundary_x(self, bar):   # bar_boundary_x - circle hits side of bar
        if bar.top_y_boundary() < self.y_pos < bar.bottom_y_boundary() + bar.length:
            if bar.right_edge_x_boundary() > self.x_pos - self.radius:
                self.change_direction_x()

    def handle_bar_boundary_y(self, bar):
        # bar_boundary - circle hits top or bottom of bar
        if bar.top_y_boundary() - bar.length < self.y_pos - self.radius < bar.bottom_y_boundary() + bar.length:
            if bar.right_edge_x_boundary() - bar.width > self.x_pos - self.radius < bar.left_x_boundary() + bar.width:
                self.change_direction_y()

    def change_direction_x(self):
        self.x_change *= -1

    def change_direction_y(self):
        self.y_change *= -1
