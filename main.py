# import modules
import pygame
import time

# import Locals
from classes.game import Game

pygame.init()

# Screen
window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Puissancfe 4")

game = Game()
game.start()

