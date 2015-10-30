__doc__ = """Main game loop and initialisation of game window"""

import pygame

import Class_Ball
import Class_Bar
from Instantiate_Initial_Objs import Draw_Init_Objs

bar_length = 100
bar_width = 10
window_width = 800
window_height = 600
FPS = 200
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
lead_y_change = 0
gameExit = False
pygame.init()
gameDisplay = pygame.display.set_mode((window_width, window_height))

def Draw_Shapes(gameDisplay, ball, lead_x, lead_y, bar_width, bar_length):
    pygame.draw.circle(gameDisplay, ball.colour, [ball.x_pos, ball.y_pos], ball.radius)
    pygame.draw.rect(gameDisplay, white, [lead_x, lead_y, bar_width, bar_length])
    # FIXME ai_bar_x,y are not defined anywhere

    pygame.draw.rect(gameDisplay, white, [ai_bar_x, ai_bar_y, bar_width, bar_length])

def initGui():
    pass

def eventLoop():
    pass

def main():

    clock = pygame.time.Clock()

    # neural network in action the longer you play the smarter it gets
    # score is a function of time played and level of iteration of neural net
    # draw diagram of neural network layers as background

    # Suggestion: You could have a method that initializes the GUI

    pygame.display.set_caption('Pong')
    pygame.display.update()

    Draw_Init_Objs(gameDisplay, white)

    # Game Loop
    while not gameExit:

        #eventLoop()

        for event in pygame.event.get():
            #pip install ipdb
            #then whenever you want to stop exectuion and inspect the program state
            #import ipdb; ipdb.set_trace() # this sets a breakpoint
            #bar_player
            # this outputs the value of the variable
            # c to continue
            # n to go to next line
            # s to step inside function
            #print('top y boundary ' + str(Class_Bar.Bar.top_y_boundary(bar_player)))
            #print('bottom y boundary ' + str(Class_Bar.Bar.bottom_y_boundary(bar_player)))
            #print((Class_Bar.Bar.top_y_boundary(bar_player)) - Class_Bar.Bar.bottom_y_boundary(bar_player)) # set up test that says that diff should equal length
            if event.type == pygame.QUIT:
                gameExit = True

        lead_y = (pygame.mouse.get_pos()[1]) - bar_length/2

        ball.update_pos()   # calls function to get new position of ball

        # ensures bar is constrained to position within window border
        lead_y, lead_y_change = update_player_bar(lead_y, lead_y_change, window_height, bar_length)

        gameDisplay.fill(black)

        Draw_Shapes(gameDisplay, ball, lead_x, lead_y, bar_width, bar_length)
        pygame.display.update()     # next frame
        clock.tick(FPS)     # fps

    pygame.quit()
    quit()

def update_player_bar(lead_y, lead_y_change, window_height, bar_length ):
    lead_y += lead_y_change
    if lead_y >= window_height - 2* bar_length or lead_y < 0:
        lead_y_change *= -1

    return lead_y, lead_y_change

if __name__ == '__main__':
    main()
