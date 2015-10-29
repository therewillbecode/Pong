__doc__ = """
Main file that creates rendering window and defines the game loop
"""
import pygame
import Class_Ball
import Class_Bar

pygame.init()
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


gameDisplay = pygame.display.set_mode((window_width, 600))

pygame.display.set_caption('Pong')

pygame.display.update()

gameExit = False

lead_y_change = 0

bar_player = Class_Bar.Bar(80, 30, 50, 300)
ball = Class_Ball.Ball(400, 300, white, 20)

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
