__author__ = 'Tom'
__doc__ = """ instantiates starting objects to be drawn when game window is initialised"""
import Class_Bar
import Class_Ball


def Draw_Init_Objs(gameDisplay, white):
    bar_player = Class_Bar.Bar(80, 30, 50, 300)
    bar_player.draw(gameDisplay, white)
    bar_ai = Class_Bar.Bar(80, 30, 730, 300)
    bar_ai.draw(gameDisplay, white)
    ball = Class_Ball.Ball(400, 300, (255, 255, 255), 20)
    ball.draw(gameDisplay)
    return bar_player, bar_ai, ball
