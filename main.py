import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from weapons import Shot


def main():
    pygame.init
    game_clock = pygame.time.Clock()
    dt = 0 
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots, updatable, drawable)
    
    AsteroidField.containers = (updatable,)  # This must be defined first!
    af1 = AsteroidField()  # Now you can create the asteroid field instance
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    print("Sprites in drawable group:", drawable.sprites())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if p1.col_check(asteroid):
                print("Game over!")
                raise SystemExit
        for asteroid2 in asteroids:
            for shot in shots:
                if shot.col_check(asteroid2):
                    print("collision detected")
                    asteroid2.split()
                    shot.kill()
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        


if __name__ == "__main__":
    main()