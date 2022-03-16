class Winner:

  def __init__(self, board_vars, board_tab):
    self.board = board_vars
    self.board_tab = board_tab

  def horizontal_winner(self):
    # No winner at beginning
    winner = ""
    # 6 lines on a puissance 4
    line = 5
    # Stop the loop
    end_game = False
    # Check every lines
    while line >= 0 and end_game == False:
      for column in range(4):
        if self.board_tab[line][column] + self.board_tab[line][column + 1] + self.board_tab[line][column + 2] + self.board_tab[line][column + 3] == self.board.red_won:
          winner = "Red"
          end_game = True
        if self.board_tab[line][column] + self.board_tab[line][column + 1] + self.board_tab[line][column + 2] + self.board_tab[line][column + 3] == self.board.yellow_won:
          winner = "Yellow"
          end_game = True
      line -= 1
        # retourne la variable winner
    return winner

  def vertical_winner(self):
    # Same logic than horizontal winner
    winner = ""
    # 7 columns
    column = 6
    end_game = False
    #Check every columns
    while column >= 0 and end_game == False:
      for line in range(3):
        if self.board_tab[line][column] + self.board_tab[line + 1][column] + self.board_tab[line + 2][column] + self.board_tab[line + 3][column] == self.board.red_won:
          end_game = True
          winner = "Red"
        if self.board_tab[line][column] + self.board_tab[line + 1][column] + self.board_tab[line + 2][column] + self.board_tab[line + 3][column] == self.board.yellow_won:
          end_game = True
          winner = "Yellow"
      column -= 1
    return winner

  def diagonal_winner(self):
    # We loop over from top left to bottom right
    winner = ""
    for line in range(3):
      for column in range(4):
        if self.board_tab[line][column] + self.board_tab[line + 1][column + 1] + self.board_tab[line + 2][column + 2] + self.board_tab[line + 3][column + 3] == self.board.red_won:
          winner = "Red"
        if self.board_tab[line][column] + self.board_tab[line + 1][column + 1] + self.board_tab[line + 2][column + 2] + self.board_tab[line + 3][column + 3] == self.board.yellow_won:
          winner = "Yellow"
    # In the second loop, it's from top right to bottom left
    for line in range(3):
      for column in range(3, 7):
        if self.board_tab[line][column] + self.board_tab[line + 1][column - 1] + self.board_tab[line + 2][column - 2] + self.board_tab[line + 3][column - 3] == self.board.red_won:
          winner = "Red"
        if self.board_tab[line][column] + self.board_tab[line + 1][column - 1] + self.board_tab[line + 2][column - 2] + self.board_tab[line + 3][column - 3] == self.board.yellow_won:
          winner = "Yellow"
    return winner


def display_winner(winner):
  if winner == "Red":
    print("Red won")
  elif winner == "Yellow":
    print("Yellow won")
   # Should not be trigger at all
  else:
    print(winner)
