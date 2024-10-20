import pygame
import Map
import Player

class Game:
    def __init__(self):
        self.map = Map.Map()
        self.display = pygame.Surface((600, 300))
        self.p = Player.Player(self)

    def mainlop(self):
        self.update()
        self.draw()

    def update(self):
        self.map.update()
        self.p.update()

    def draw(self):
        self.display.fill((0,0,0))
        self.map.draw(self.display)
        self.p.draw(self.display)


