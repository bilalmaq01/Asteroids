import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bg_image = pygame.image.load('background.jpeg')


    Player.containers = (updatable, drawable)
    Asteroid.containers =(asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots,updatable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        screen.blit(bg_image,(0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for ass in asteroids:
            uhohcheck = ass.collision(player)
            if uhohcheck == True:
                print("Game Over!")
                print(score)
                sys.exit()
        
        for ass in asteroids:
            for bull in shots:
                bullcheck = bull.collision(ass)
                if bullcheck == True:
                   bull.kill()
                   ass.split()
                   score += 10

        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)

        for obj in drawable:
            obj.draw(screen)

        screen.blit(score_text, score_rect)


        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()