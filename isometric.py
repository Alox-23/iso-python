import pygame
import math
from perlin_noise import PerlinNoise

pygame.init()

screen = pygame.display.set_mode((1200, 600))
display = pygame.Surface((200, 100))

class Cube:
    def __init__(self, worldpx, worldpy, worldpz) -> None:
        self.image = pygame.image.load("green-cube.png")
        self.rect = self.image.get_rect()

        self.world_pos_x = worldpx
        self.world_pos_y = worldpy
        self.world_pos_z = worldpz

    def update_screen_pos(self):
        self.rect.x = self.world_pos_x*0.5*32 + self.world_pos_y*-0.5*32 -16 + 100
        self.rect.y = self.world_pos_x*0.25*32 + self.world_pos_y*0.25*32 + self.world_pos_z*32 -50

    def update(self):
        self.update_screen_pos()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
n = PerlinNoise(octaves=3)
world = []
world_size = 20
for i in range(world_size):
    world.append([])
    for j in range(world_size):
        world[i].append(Cube(j, i, 0+n.noise([i/world_size, j/world_size])))

running = True

clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display.fill((0, 0, 255))

    #update and draw world()
    for i in world:
        for j in i:
            j.update()
            j.draw(display)

    pygame.display.set_caption(str(int(clock.get_fps())))

    screen.blit(pygame.transform.scale(display, (1200, 700)), (0,0))
    pygame.display.update()