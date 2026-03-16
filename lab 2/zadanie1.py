import pygame
import math
import sys

pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))

CZARNY = (30,30,30)
BIALY = (255,255,255)
NIEBIESKI = (0,0,255)
CYAN = (0,255,255)
FIOLET = (150,100,255)
CZERWONY = (255,100,100)
ZIELONY = (100,255,100)
POMARANCZOWY = (255,165,0)

current_variant = 1


def get_heptagon_points(radius, stretch_x=1.0, rotation_deg=0, shear_factor=0):

    points = []
    rad_rot = math.radians(rotation_deg)

    for i in range(7):

        angle = math.radians(360/7 * i)

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        x = x * stretch_x
        x = x + shear_factor * y

        rx = x * math.cos(rad_rot) - y * math.sin(rad_rot)
        ry = x * math.sin(rad_rot) + y * math.cos(rad_rot)

        points.append((rx,ry))

    return points


def draw_variant(variant):

    radius = 100
    stretch = 1
    rotation = 0
    shear = 0
    color = NIEBIESKI

    if variant == 2:
        radius = 250
        rotation = 45
        color = CYAN

    elif variant == 3:
        radius = 150
        rotation = 180

    elif variant == 4:
        radius = 120
        shear = 0.5

    elif variant == 5:
        stretch = 2.5
        color = FIOLET

    elif variant == 6:
        shear = 1
        rotation = 58
        color = CZERWONY

    elif variant == 7:
        radius = 150
        rotation = 180

    elif variant == 8:
        stretch = 2.5
        rotation = 45
        color = ZIELONY

    elif variant == 9:
        rotation = 90
        color = POMARANCZOWY


    points = get_heptagon_points(radius, stretch, rotation, shear)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    offset_x = width//2
    offset_y = height//2

    if variant == 5:
        offset_y = -min_y
        offset_x = width//2

    elif variant == 8:
        offset_x = -min_x
        offset_y = height - max_y

    elif variant == 9:
        offset_x = width - max_x
        offset_y = height//2


    draw_points = [(p[0]+offset_x, p[1]+offset_y) for p in points]

    pygame.draw.polygon(win, color, draw_points)
    pygame.draw.polygon(win, BIALY, draw_points, 2)


run = True

while run:

    win.fill(CZARNY)

    draw_variant(current_variant)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1: current_variant = 1
            if event.key == pygame.K_2: current_variant = 2
            if event.key == pygame.K_3: current_variant = 3
            if event.key == pygame.K_4: current_variant = 4
            if event.key == pygame.K_5: current_variant = 5
            if event.key == pygame.K_6: current_variant = 6
            if event.key == pygame.K_7: current_variant = 7
            if event.key == pygame.K_8: current_variant = 8
            if event.key == pygame.K_9: current_variant = 9