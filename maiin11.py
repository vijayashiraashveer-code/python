import pygame 
import randompygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT =pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW  = pygame.Color('yellow')
MAGENTA = pygame.Color('MAGENTA')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
   def__init__(self,color,height,width):
     super().__init__()
     self.image = pygame.surface([width,height])
     self.image.fill(color)
     self.rect = self.image.get_rect()
     self.velocity = [random.choices([-1,-1]),random.choice([-1,-1])]
   def updates(self):
     self.rect.move_ip(self.velocity)
     boundry_hit =False
     if self.rect.left <=0 or self.rect.right >= 500
     self.velocity[0] = -self.velocity[0]
     boundry_hit = True
    if self.recttop <= 0 or self.rect.bottom >= 400:
        self.velocity[1] = 
