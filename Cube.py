import pygame

class Cube:
    def __init__(self, worldpx, worldpy, worldpz) -> None:
        self.image = pygame.image.load("green-cube.png")
        self.rect = self.image.get_rect()

        self.world_pos_x = worldpx
        self.world_pos_y = worldpy
        self.world_pos_z = worldpz

    def update_screen_pos(self):
        self.rect.x = self.world_pos_x*0.5*32 + self.world_pos_y*-0.5*32 -16 + 300
        self.rect.y = self.world_pos_x*0.25*32 + self.world_pos_y*0.25*32 + self.world_pos_z*32

    def update(self):
        self.image = pygame.image.load("green-cube.png")
        self.update_screen_pos()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_world_pos(self):
        return  pygame.math.Vector3(self.world_pos_x, self.world_pos_y, self.world_pos_z)
    
    def change_color(self):
        self.image = pygame.image.load("isometric-tiles/orange-indiv/orange-cube.png")