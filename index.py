import pygame
pygame.init()
import Class_Ball
import Class_Bar

from Instantiate_Initial_Objs import Draw_Init_Objs

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


def Draw_Shapes():
    pygame.draw.circle(gameDisplay, ball.colour, [ball.x_pos, ball.y_pos], ball.radius)
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, bar_width, bar_length])
    pygame.draw.rect(gameDisplay, white, [ai_bar_x, ai_bar_y, bar_width, bar_length])

gameDisplay = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Pong')

pygame.display.update()

gameExit = False


lead_y_change = 0

Draw_Init_Objs()

# Game Loop
while not gameExit:

    for event in pygame.event.get():
        print('top y boundary ' + str(Class_Bar.Bar.top_y_boundary(bar_player)))
        print('bottom y boundary ' + str(Class_Bar.Bar.bottom_y_boundary(bar_player)))
        print((Class_Bar.Bar.top_y_boundary(bar_player)) - Class_Bar.Bar.bottom_y_boundary(bar_player)) # set up test that says that diff should equal length
        if event.type == pygame.QUIT:
            gameExit = True

    lead_y = (pygame.mouse.get_pos()[1]) - 50

    ball.update_pos()   # calls function to get new position of ball

    # ensures bar is constrained to position within window border
    lead_y += lead_y_change
    if lead_y >= 495 or lead_y < 0:
        lead_y_change *= -1

    gameDisplay.fill(black)

    Draw_Shapes()
    pygame.display.update()     # next frame
    clock.tick(200)     # fps

pygame.quit()
quit()
