import pygame
import sys
import random
import math
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWWHEIGHT = 650
FPS = 60
SIZE = 4.5  # kích thước viên đạn nổ ra
SPEED_CHANGE_SIZE = 0.05  # Tốc độ nhỏ lại của viên đạn khi nổ ra
CHANGE_SPEED = 0.07  # Tốc độ chậm lại của viên đạn
RAD = math.pi/180  # Đổi từ radian sang độ
A_FALL = 1.5  # Gia tốc rơi tự do
NUM_BULLET = 50  # Số đạn nổ ra trong 1 quả pháo
SPEED_MIN = 2  # Tốc độ nhỏ nhất của 1 viên đạn
SPEED_MAX = 4  # Tốc độ lớn nhất của 1 viên đạn
TIME_CREATE_FW = 40 #Khoảng thời gian liên tiếp giữa 2 lần bắn
NUM_FIREWORKS_MAX