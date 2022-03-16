import pygame

from classes.board import Board


class GridView:

  def __init__(self):
    self.player = 1
    self.game_board = Board()
    # on init pygame une seule fois
    self.game = pygame
    self.column = 0
    pygame.init()
    # Taille du plateau
    self.grid_picture = self.game.image.load('assets/grid.png')
    width = self.grid_picture.get_size()
    self.board_width = (width[0], width[1])
    # Set notre écran de jeu
    self.screen = self.game.display.set_mode(self.board_width)
    self.screen.blit(self.grid_picture, (0, 0))
    self.game.display.flip()

    # Yellow token picture
    self.yellow_token_pic = self.game.image.load('assets/yellow.png')
    # Red token
    self.red_token_pic = self.game.image.load('assets/red.png')
    # Font
    self.font = self.game.font.Font(None, 25)

  def get_column(self, number):
    column = number - 16
    column = int(column / 100)
    if column in range(0, 7):
      if self.game_board.board[5][int(column)] == 0:
        self.column = column
    return column

  def render(self, board):
    # Refresh the screen
    self.screen.fill((0, 0, 0))
    self.screen.blit(self.grid_picture, (0, 0))
    revert = self.game_board.revert_board(board)
    # On re parcourt le board pour le render
    for i in range(len(revert)):
      for j in range(len(revert[i])):
        # Red token
        if revert[i][j] == self.game_board.red_token:
          self.screen.blit(self.red_token_pic, (16 + 97 * j, 13 - 97 * i + 486))
        self.game.display.flip()
        # Yellow token
        if revert[i][j] == self.game_board.yellow_token:
          self.screen.blit(self.yellow_token_pic, (16 + 97 * j, 13 - 97 * i + 486))
        self.game.display.flip()
