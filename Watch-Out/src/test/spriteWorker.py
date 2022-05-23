
import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load("Watch-Out/src/test/doux.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)
animationList=[]
step=10
lastUpdate=pygame.time.get_ticks()
animationCooldown=100
frame=0

for x in range (step):
    animationList.append(sprite_sheet.get_image(x, 24, 24, 3, BLACK))

run = True
while run:

	#update background
    screen.fill(BG)
    currentTime = pygame.time.get_ticks()
    if currentTime-lastUpdate >= animationCooldown:
        frame+=1
        lastUpdate=currentTime
        if frame >= len(animationList):
            frame=0
    screen.blit(animationList[frame], (0, 0))
	#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()