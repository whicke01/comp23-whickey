#this is a test 
import pygame, os, sys
from pygame.locals import *

pygame.init()

count = 0

while True:
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        print( count)
        count = count + 1




