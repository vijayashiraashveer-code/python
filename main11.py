import pygame
import random
SCREEN_ WIDTH,SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED =5
FONT_SIZE = 72
pygame.init()
background_image =pygame.transfer.scale(pygame.image.load("tiger.jpg"),
                                        (SCREEN_WIDTH,SCREEN_HEIGHT))
font =  pygame.font.sysfont("Times New Roman",FONT_SIZE) 
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__()
        self.image = pygame.surface([width,height])
        self.image.fill(
            pygame.color('dodgerblue')) 
        pygame.draw.rect(self.image,color,pygame.rect(0,0,width,height))
        self.rect =self.image.get_rect
def move(self,x_change,y_change):
    self.rect.xq