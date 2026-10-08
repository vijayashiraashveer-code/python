import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT=500
PLAYER_START_X = 370
PLAYER_START_Y = 390
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX =150
ENEMY_SPEED_X = 4
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_model((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('x.jpg')
pygame.display.set_caption("space invader")
icon = pygame.image.load('x.jpg')
pygame.display.set_caption(icon)
playeIMG = pygame.image.load('tiger.jpg')
playerx = PLAYER_START_X
playery= PLAYER_START_Y
playerx_change = 0
enemyIMG = []
enemyX = []
enemy=[]
num_of_enemies = 6
for _1 in range(num_of_enemies):
    enymyIMG.append(pygame.image.load('x.jpg'))
    enymyx.append(random.randint(0, SCREEN_WIDTH - 64 ))
    enemyy.append(random.randint(ENEMY_START_Y_MIN,
    ENEMY_START_Y_MAX))
    enemyY_change.append(ENEMY_SPEED_X)
    enemyX_change.append(ENEMY_SPEED_Y)

    bulletIMG = pygame.image.load('bullet.png')
    bulletx = 0
    bulletY_change = speedY
scorevalue= 0 
font =pygame.font.Font('freesansbold.ttf',64)
 def showscore(x,y)
