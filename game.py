import pygame
from pygame.locals import *
import random

#variables

start=True
game= True
size=width, height=(1200,520)
window = pygame.display.set_mode(size)
pygame.display.set_caption("CAR BUMP")
window.fill((210,187,156))
top=(width,height/5.2)
bottom=(width,height/1.6)

top2=(width+600,height/5.2)
bottom2=(width+600,height/1.6)

side=100
topright=(side,height/5.2)
topleft=(side/2,height/5.2)

#CLOCK
clock=pygame.time.Clock()

usertop=(0,height/5.2)
userbottom=(0,height/1.6)
run=True
run2=True
#images and resources
c= pygame.image.load("ob2.png")
car=c.get_rect()
car.topleft=(usertop)

c2= pygame.image.load("ob1.png")
car2=c2.get_rect()
car2.topright=(bottom)

road= pygame.image.load('road.jpg')
roadl=road.get_rect()
roadl.topleft=(0,0)

c3=pygame.image.load("ob3.png")
car3=c.get_rect()
car3.topright=(top2)

road2= pygame.image.load('road.jpg')
road3=road.get_rect()
road3.topleft=(700,0)

s= pygame.image.load("start.jpg")
start=s.get_rect()
start.topleft=(0,0)

o= pygame.image.load('over.jpg')
over=o.get_rect()
over.topleft=(0,0)
#loops

#start screen loop

while start:
    for event in pygame.event.get(): 
        if event.type == QUIT:
          game= False
          start=False
    if run:           
     speed=-1
     window.blit(s,start)
     if event.type==KEYUP:
            if event.key in [K_SPACE]:
             start=False
    #clock.tick(60)
    pygame.display.update()
#game loop
while game:
    for event in pygame.event.get():
        if event.type == QUIT:
          game= False
        if run:
         if event.type==KEYDOWN:
            if event.key in [K_s,K_DOWN]:
             car=car.move(userbottom)
             if event.key in[K_s,K_DOWN]:
                car.topleft=(userbottom)
         if event.type==KEYDOWN:
            if event.key in [K_w,K_UP]:
             car=car.move(usertop)
             if event.key in[K_w,K_UP]:
                car.topleft=(usertop) 
    if run:          
     speed=-1
     level=0
     window.blit(road,roadl)
     window.blit(road2,road3)
     window.blit(c,car)
     car3.x+=speed
     if car3.x==-800:
        if random.randint(0,1)==0:
         car3.topleft=(top2)
        else:
         car3.topleft=(bottom2)
         car3.x=1200
     window.blit(c3,car3)
     car2.x+=speed
     if car2.x==-800:
        if random.randint(0,1)==0:
         car2.topleft=(bottom)
        else:
         car2.topleft=(top)  
         car2.x=1200
     window.blit(c2,car2)
     if car.colliderect(car3) or car2.colliderect(car):
        run=False
    else:
       window.blit(o,over)
    if event.type==KEYDOWN and event.key in[K_KP_ENTER]:
            run=True
            car2.topright=(bottom)
            car.topleft=(usertop)
            car3.topleft=(top2)
    if event.type==KEYDOWN and event.key in[K_RETURN]:
            run=True
            car2.topright=(bottom)
            car.topleft=(usertop)
            car3.topleft=(top2)
    pygame.display.update()
pygame.quit()