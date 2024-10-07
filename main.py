import pygame
from player import *
from constants import *

def main():
 print("Starting asteroids!")
 print(f"Screen width: {SCREEN_WIDTH}")
 print(f"Screen height: {SCREEN_HEIGHT}")

 pygame.init()
 screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 clock = pygame.time.Clock()
 playr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
 dt = 0

 


 while True:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    return
  screen.fill((0,0,0))
  playr.draw(screen)
  playr.update(dt)
  pygame.display.flip()
  
  dt = clock.tick(60) / 1000
 

if __name__ == "__main__":
 main()
