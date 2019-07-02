import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.Info()

#set width and height to screen size
size = (width,height) = (int(screen.current_w), int(screen.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 225)

# load image and rect
sprite_image = pygame.image.load("seal-monk.png")
sprite_image = pygame.transform.smoothscale(sprite_image, (80,80))
sprite_rect = sprite_image.get_rect()

sprite_rect.center = (width // 2, height // 2)

speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
sprite_image = pygame.transform.rotate(sprite_image, 180 - rotation)


def move_sprite():
    sprite_rect.move_ip(speed)


def main():
    while True:
        clock.tick(60)
        move_sprite()
        screen.fill(color)
        screen.blit(sprite_image, sprite_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()