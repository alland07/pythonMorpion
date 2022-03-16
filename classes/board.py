import pygame
from pygame import surface
class Board:
  empty = 0
  yellow_token = 1
  red_token = -1
  yellow_won = 4
  red_won = -4

  def __init__(self):
    self.board = [
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
    ]

  def display(self):
    print("\n")
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        print(self.board[i][j], end=' ')
      print()
    print("\n")