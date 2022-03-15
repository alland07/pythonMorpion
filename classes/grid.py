import pygame
from pygame import surface


class Plateau:
  case_width = 100
  nb_lignes = 6
  nb_colonnes = 7

  rayon = (case_width/2)-6

  width = nb_colonnes * case_width
  height = (nb_lignes + 1) * case_width
  volume = (width, height)
  screen = pygame.display.set_mode(volume)

  bleu = pygame.Color(0, 0, 255)
  noir = pygame.Color(0, 0, 0)

  def __init__(self):
    # background
    pygame.draw.rect(
      self.screen,
      self.bleu,
      ((0, 50), (self.width + 100, self.height))
    )
    # Cases
    for c in range(self.nb_colonnes):
      for r in range(self.nb_lignes):
        pygame.draw.circle(
          self.screen,
          self.noir,
          ((c * self.case_width + self.case_width), (r * self.case_width + self.case_width + self.case_width)),
          self.rayon)
    pygame.display.flip()

  def updatePlateau(self):
    pygame.display.update()
