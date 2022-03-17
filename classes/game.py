import sys

from classes.gridView import *
from classes.winner import display_winner


class Game:
  max_token = 42

  def __init__(self):
    self.played_token = 0
    self.winner = False
    self.grid = GridView()
    self.board = Board()

  def get_player(self):
    # Which Player is it
    if self.played_token % 2 == 0:
      number = self.board.red_token
    else:
      number = self.board.yellow_token
    return number

  def start(self):
    pygame.init()
    while self.winner != "Yellow" and self.winner != "Red" and self.played_token < self.max_token:
      # players play
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          # Get mouse position on the grid
          x, y = pygame.mouse.get_pos()
          # Get current user
          player = self.get_player()
          # Get current column used
          column = self.grid.get_column(x)
          # Play a token for the user
          played_token = self.board.play_token(player, column)
          # Check if we get a winner
          if played_token:
            self.played_token += 1
            self.winner = self.board.get_winner()
            # Display again the grid
            self.grid.render(self.board.board)
            self.grid.game.display.flip()

        # Close the game
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            # Press escape
            pygame.quit()
        elif event.type == pygame.QUIT:
          # Quit event
          pygame.quit()
          sys.exit()

    display_winner(self.winner)
