import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroid_group, update_group, draw_group)
    AsteroidField.containers = (update_group)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in update_group:
            obj.update(dt)
        for ast in asteroid_group:
            if ast.collision(player):
                print("Game Over")
                sys.exit()
        screen.fill((0,0,0))
        for obj in draw_group:
            obj.draw(screen)
        pygame.display.flip()
        dt = my_clock.tick(60) / 1000

if __name__ == "__main__":
    main()