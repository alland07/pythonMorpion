import pygame

from classes.board import *
from classes.gridView import *


class Game:
  max_token = 42

  def __init__(self):
    self.player = 1
    self.played_token = 0
    self.winner = False
    self.gameView = GridView()
    self.board = Board()

  def get_player(self):
    # Which Player is it
    if self.played_token % 2 == 0:
      number = self.board.red_token
    else:
      number = self.board.yellow_token
    return number

  def start(self):
    while self.winner != "Yellow" and self.winner != "Red" and self.played_token < self.max_token:
      # players play
      for event in pygame.event.get():
        self.board.display()
        if event.type == pygame.MOUSEBUTTONUP:
          x, y = pygame.mouse.get_pos()
          player = self.get_player()
        elif event.type == event.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.exit()
        elif event.type == pygame.QUIT:
          pygame.exit()

