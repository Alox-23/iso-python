import pygame
import Game

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

g = Game.Game()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    g.mainlop()

    pygame.display.set_caption(str(int(clock.get_fps())))

    screen.blit(pygame.transform.scale(g.display, (1200, 700)), (0,0))
    pygame.display.update()