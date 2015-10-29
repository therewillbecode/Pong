import pygame
pygame.init()
import random as r
import sys
import sys
sys.path.append('C:\Users\Tom\PycharmProjects\untitled3')
import NN_output

clock = pygame.time.Clock()

# neural network in action the longer you play the smarter it gets
# score is a function of time played and level of iteration of neural net
# draw diagram of neural network layers as background

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
window_width = 800
window_height = 600

bar_length = 100
bar_width = 10

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
                self.change_direction_x()

        # bar_boundary_y - circle hits top or bottom of bar
        if lead_y - bar_length < self.y_pos - self.radius < lead_y + bar_length:
            if lead_x - bar_width > self.x_pos - self.radius < lead_x + bar_width:
                self.change_direction_y()

    def change_direction_x(self):
        self.x_change *= -1

    def change_direction_y(self):
        self.y_change *= -1


class Bar:

    x_pos_center = (pygame.mouse.get_pos()[1]) - 50

    def __init__(self, length, width, start_x, start_y):
        self.x_pos_center = start_x
        self.y_pos_center = start_y
        self.length = length
        self.width = width
        pygame.draw.rect(gameDisplay, white, [start_x, start_y,
                                              width, length])

    def right_edge_x_boundary(self):
        return self.x_pos_center + (0.5 * self.width)

    def left_x_boundary(self):
        return self.x_pos_center - (0.5 * self.width)

    def top_y_boundary(self):
        return self.x_pos_center - (0.5 * self.length)

    def bottom_y_boundary(self):
        return self.x_pos_center + (0.5 * self.length)


gameDisplay = pygame.display.set_mode((window_width, 600))

pygame.display.set_caption('Dwelling')

pygame.display.update()

gameExit = False



lead_y_change = 0

bar_player = Bar(80, 30, 50, 300)
ball = Ball(400, 300, white, 20)

lead_x = bar_player.x_pos_center
lead_y = bar_player.y_pos_center
# Game Loop
while not gameExit:

    for event in pygame.event.get():
        #  print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lead_y_change = -4
            if event.key == pygame.K_DOWN:
                lead_y_change = 4
    lead_y = (pygame.mouse.get_pos()[1]) - 50

    # speed at which ball moves from initial position
    ball.update_pos()

    lead_y += lead_y_change
    if lead_y >= 495 or lead_y < 0:
        lead_y_change *= -1

    gameDisplay.fill(black)
    pygame.draw.circle(gameDisplay, ball.colour, [ball.x_pos, ball.y_pos], ball.radius)
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, bar_width, bar_length])
   # pygame.draw.rect(gameDisplay, white, [bar_player.x_pos_center, bar_player.y_pos_center,
    #                                      bar_width, bar_length])

    # push  input data for NN to array for given frame(ball centre pos + player bar y_pos)
    pygame.display.update()
    clock.tick(200)

pygame.quit()
quit()
