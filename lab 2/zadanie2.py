import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zadanie 2")

# kolory
NIEBIESKI = (0, 0, 255)
BIALY = (255,255,255)
CZARNY = (0,0,0)

shape = pygame.Surface((600, 600), pygame.SRCALPHA)

pygame.draw.rect(shape, NIEBIESKI, (100, 200, 400, 200))

pygame.draw.polygon(shape, NIEBIESKI, ([300, 200], [200, 0], [400, 0]))

pygame.draw.polygon(shape, NIEBIESKI, ([300, 400], [200, 600], [400, 600]))

final_shape = pygame.transform.scale(shape, (600, 600))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill(BIALY)

    win.blit(final_shape, (0,0))

    pygame.display.update()