# imports
import pygame, sys
from pygame.locals import *

# initalize pygame
pygame.init()

# assign FPS(frame per second)
FPS = 30
clock = pygame.time.Clock()

#setup colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# display dimensions
SCREEN_WIDTH = 300
height = 300
# setup a 300x300 pixel display
displaysurf = pygame.display.set_mode((width, height))
displaysurf.fill(WHITE)
pygame.display.set_caption("my drawing")

import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
     
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
# create lines and shapes
pygame.draw.line(displaysurf, BLUE, (150, 130), (130, 170)) #coordinate points (starting point), (ending point)
pygame.draw.line(displaysurf, BLUE, (150, 130), (170, 170))
pygame.draw.line(displaysurf, GREEN, (130, 170), (170, 170))
pygame.draw.circle(displaysurf, BLACK, (100,50), 30)
pygame.draw.circle(displaysurf, BLACK, (200,50), 30)
pygame.draw.rect(displaysurf, RED, (100, 200, 100, 50), 2) #(x point of top left corner, y point of top left corner, length , how tall is it) how think outline)
pygame.draw.rect(displaysurf, BLACK, (110, 260, 80, 5)) #no other number after = fill in shape

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #quits the game
            sys.exit()

    # refreshing display/screen
    pygame.display.update()
    clock.tick(FPS)