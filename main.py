import pygame
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
 print("Starting asteroids!")
 print(f"Screen width: {SCREEN_WIDTH}")
 print(f"Screen height: {SCREEN_HEIGHT}")

 pygame.init()
 screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 clock = pygame.time.Clock()



 updatable = pygame.sprite.Group()
 drawable = pygame.sprite.Group()
 asteroids = pygame.sprite.Group()
 shots = pygame.sprite.Group()

 Player.containers = (updatable, drawable)

 Asteroid.containers = (asteroids, updatable, drawable)
 AsteroidField.containers = updatable
 asteroid_field = AsteroidField()
 Shot.containers = (shots, updatable,drawable)
 playr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
 dt = 0
 


 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    return
  
  
  for object in updatable:
   object.update(dt)

  for asteroid in asteroids:
   if asteroid.collision_detect(playr):
    print("Game over!")
    exit()
   for shot in shots:
    if asteroid.collision_detect(shot):
     shot.kill()
     asteroid.split()

  screen.fill((0,0,0))
  for object in drawable:
   object.draw(screen)
  
  pygame.display.flip()
  
  dt = clock.tick(60) / 1000
 

if __name__ == "__main__":
 main()
