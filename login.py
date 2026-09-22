import pygame #import neccesary libraries
# initalize required mo
pygame.init()
# setup window geometry
screen = pygame.display.set_mode((400,500))
# create a loop to run til the game is quit by the user
pygame.display.set_caption('ading image and baground image')
baground image = pygame.transform.scale pygame.image.load
done = False 
while not done :
    for event in pygame.event.get():
        if event.i==event.quit:
            pygame.quit()
    pygame.display.flip()


