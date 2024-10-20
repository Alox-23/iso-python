import pygame
import math 

class Player:
    def __init__(self, g):
        self.game = g
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.speed = 0.07
        self.gravity = 0.006

        self.world_pos_x = 2
        self.world_pos_y = 2
        self.world_pos_z = 0
        self.floor = 0
        self.delta_z = 0
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.world_pos_x -= self.speed
        elif keys[pygame.K_DOWN]:
            self.world_pos_x += self.speed
        elif keys[pygame.K_LEFT]:
            self.world_pos_y += self.speed
        elif keys[pygame.K_RIGHT]:
            self.world_pos_y -= self.speed

        if keys[pygame.K_SPACE]:
            self.delta_z = -0.1

        self.delta_z += self.gravity
        if self.delta_z > 0.5: 
            self.delta_z = 0.5

        self.world_pos_z += self.delta_z

        if self.floor < self.world_pos_z:
            self.delta_z = 0
            self.world_pos_z = self.floor

    def update(self):
        self.floor = self.game.map.get_tile(int(self.world_pos_x+1), int(self.world_pos_y+1), int(self.world_pos_z)).get_world_pos().z
        self.game.map.get_tile(int(self.world_pos_x+1), int(self.world_pos_y+1), int(self.world_pos_z)).change_color()
        self.rect.x = self.world_pos_x*0.5*32 + self.world_pos_y*-0.5*32 -16  + 300
        self.rect.y = self.world_pos_x*0.25*32 + self.world_pos_y*0.25*32 + self.world_pos_z*32 -8

        self.handle_input()

        print(int(self.world_pos_x+0.75), int(self.world_pos_y+0.75), int(self.world_pos_z))
    
    def draw(self, d):
        d.blit(self.image, self.rect)
        