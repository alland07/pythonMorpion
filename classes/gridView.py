import pygame

from classes.board import Board


class GridView:

  def __init__(self):
    self.player = 1
    self.gameboard = Board()
    self.game = pygame

    pygame.init()
    # Taille du plateau
    board_picture = pygame.image.load('assets/grid.png')
    x = 1
    self.board_width = (board_picture[0], board_picture[1])
    # Set notre écran de jeu
    self.screen = pygame.display.set_mode(self.board_width)
    self.screen.blit(board_picture, (0, 0))
    pygame.display.flip()

    # Yellow token
    self.yellow_token = pygame.image.load('assets/yellow.png')
    # Red token
    self.red_token = pygame.image.load('assets/red.png')
    # Font
    self.font = pygame.font.Font(None, 25)