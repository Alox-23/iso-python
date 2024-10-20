import pygame
from perlin_noise import PerlinNoise
import Cube

class Map:
    def __init__(self):
        self.n = PerlinNoise(octaves=2)
        self.world = []
        self.world_size_x = 20
        self.world_size_y = 20
        self.world_size_z = 1
        self.generateWorld()

    def generateWorld(self):
        for z in range(self.world_size_z):
            self.world.append([])
            for y in range(self.world_size_y):
                self.world[z].append([])
                for x in range(self.world_size_x):
                    if x > 5:
                        self.world[z][y].append(Cube.Cube(x, y, 2))
                    else:
                        self.world[z][y].append(Cube.Cube(x, y, 0))

    def update(self):
        for k in self.world:
            for i in k:
                for j in i:
                    j.update()
                
    def draw(self, display):
        for k in self.world:
            for i in k:
                for j in i:
                    j.draw(display)

    def get_tile(self, x, y, z):
        return self.world[len(self.world)-1][y][x]