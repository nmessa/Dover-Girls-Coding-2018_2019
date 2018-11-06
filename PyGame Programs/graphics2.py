##Lab Exercise 11.1.2018 Problem 2
##Author: nmessa
##File: graphics2.py

import pygame, sys, random
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([1024, 768])
screen.fill([255, 255, 255])
for i in range (100):
    width = random.randint(100, 250)
    height = random.randint(50, 100)
    top = random.randint(0, 650)
    left = random.randint(0, 800)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_width = random.randint(1, 3)
    #pygame.draw.rect(screen, color, [left, top, width, height], line_width)
    pygame.draw.ellipse(screen, color, [left, top, width, height], line_width)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
