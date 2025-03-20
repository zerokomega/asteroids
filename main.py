import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_for_collision(asteroid):
                    asteroid.split()
                    shot.kill()
            if player.check_for_collision(asteroid):
                game_over()
            

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def game_over():
    print("Game over!")
    sys.exit()

if __name__ == "__main__":
    main()