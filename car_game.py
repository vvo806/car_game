# imports
import pygame, sys
from pygame.locals import *
import random, time

from Game import SCREEN_HEIGHT

# initalize pygame
pygame.init()

# assign FPS(frame per second)
FPS = 30 #30 frames per second
clock = pygame.time.Clock()
"""
FPS = pygame.time.Clock()
FPS.tick(30)
"""

#setup colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# display dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#setting up fonts OUTSIDE of game
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK) #creates graphics for fonts
 
background = pygame.image.load("AnimatedStreet.png")
 
# setup a 300x300 pixel display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite): #sprite means this class a child class
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect() #get_rect automatically make the rectangle same size as image
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) #defines starting point for rect
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,10) # (distance to be moved in X direction, distance to be moved in Y direction); makes car move 10 pixels down
        if (self.rect.bottom > 600): # when end of car moves out of screen
            SCORE += 1 # score adds when you avoided the top
            self.rect.top = 0 # top of car back at top
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0) #car appears at random locations
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    # allows the player to click the direction keys to move car 
    def move(self): 
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        # ensures player dont move off screen
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
            
    # drawing car on surface of image
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()

#creating Sprite groups
#created two groups (enemies and all_sprite)
#use add() function to add sprite to a group
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1) 
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1 #custom created an event called INC_SPEED; number is just event ID
pygame.time.set_timer(INC_SPEED, 1000) #calling the event every 1000 milliseconds (1 second)
 
#Game Loop
while True:
       
    # Cycles through all events occuring  
    for event in pygame.event.get(): #pygame.event.get() calls to perform an action on keyboard; #iterating over every event that occurred
        if event.type == INC_SPEED:
              SPEED += 4 #increases speed of enemy by variable of 4
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.fill(WHITE) #to refresh screen white
 
    #Moves and Re-draws all Sprites
    #we call move() function and redraw the sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies): #checks to see whether Player has hit any sprite in "enemies" group
        pygame.mixer.Sound('crash.wav').play() #sound() loads crash sound in game once collied; #play() plays the sound
        time.sleep(0,5)

        DISPLAYSURF.fill(RED) #to refresh screen red
        DISPLAYSURF.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill() #if collision true, kill all sprites (removes sprite from group)
        time.sleep(2)
        pygame.quit() #to close game window
        sys.exit()        
         
    pygame.display.update() #updates game since values change
    clock.tick(FPS)
