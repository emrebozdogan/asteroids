# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updateble = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    AsteroidField.containers = updateble
    Asteroid.containers = (asteroid, updateble, drawable)
    Player.containers = (updateble, drawable)
    Shot.containers = (shot, updateble, drawable)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill(color="black")
        
        # Update all sprites in updateble group
        updateble.update(dt)
        
        for sprite in asteroid:
            if player.collision(sprite):
                print("Game Over!")
                pygame.quit()
            
            for bullet in shot:
                if sprite.collision(bullet):
                    sprite.split()
                    bullet.kill()
                    
        # Draw all sprites in drawable group
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()