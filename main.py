# import modules
import pygame
from classes.game import Game

pygame.init()

# Screen
window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Puissance 4")


def play_game():
  game = Game()
  game.start()


play_game()
