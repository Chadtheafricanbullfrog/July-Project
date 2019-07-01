import pygame
from pygame.locals import*

pygame.init()
screen = pygame.display.info()

#set width and height to screen size
size = (width,height) = (int(screen.current_w), int(screen.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 225)

def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display.flip()




