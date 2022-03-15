# import modules
import pygame
import time

# import Locals
from classes.grid import Plateau

# Screen
pygame.display.set_mode((800, 750))
pygame.display.set_caption("Puissance 4")

# Init Game Plateau
plateau = Plateau()

loop = True
endGame = False

while loop:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_j:
          endGame = True
          loop = False


def closeScreen():
  pygame.quit()


# Close the game
if endGame:
  closeScreen()
