__author__ = 'Tom'
__doc__ = """ instantiates starting objects to be drawn when game window is initialised"""
import Class_Bar
import Class_Ball


def Draw_Init_Objs():
    bar_player = Class_Bar.Bar(80, 30, 50, 300)
    bar_ai = Class_Bar.Bar(80, 30, 730, 300)
    ball = Class_Ball.Ball(400, 300, (255, 255, 255), 20)
