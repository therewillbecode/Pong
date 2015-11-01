__author__ = 'Tom'
from random import gauss
import random
import math


def rand(ball):
    return int(math.floor((gauss(ball.y_pos, 1))))


