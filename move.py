import pygame, sys
import pygame.locals

pygame.init()
BLACK = (0,0,0)
WIDTH = 1280
HEIGHT = 1024
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)

while True:
    for event in pygame.event.get():
        if event.key == pygame.K_p: # replace the 'p' to whatever key you wanted to be pressed
             pass
             print("worked")
        if event.type == pygame.locals.QUIT:
             pygame.quit()
             sys.exit()