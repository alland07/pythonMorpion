from classes.winner import *


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
    self.current_winner = Winner(Board, self.board)

  def get_winner(self):
    # Check every case
    winner = self.current_winner.horizontal_winner()
    if winner != "":
      return winner
    winner = self.current_winner.vertical_winner()
    if winner != "":
      return winner
    winner = self.current_winner.diagonal_winner()
    if winner != "":
      return winner
    else:
      return False

  def play_token(self, gamer, column):
    line = 5
    put = False
    while line >= 0 and not put:
      if self.board[line][column] == self.empty:
        if gamer == self.red_token:
          self.board[line][column] = self.red_token
          put = True
        elif gamer == self.yellow_token:
          self.board[line][column] = self.yellow_token
          put = True
      if line > 0:
        line -= 1
      elif line == 0 and not put:
        return False
    return True

  def revert_board(self, old_board):
    revert_board = []
    for row in range(5, -1, -1):
      revert_board.append(old_board[row])
    return revert_board
