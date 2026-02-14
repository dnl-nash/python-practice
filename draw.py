import pygame
import argparse
import random
import time
import sys
pygame.display.init()
parser=argparse.ArgumentParser()
parser.add_argument("-d","--desktop")
parser.add_argument("-s","--speed")
parser.add_argument("-n","--num")
settings=parser.parse_args()
desktop=settings.desktop
if(desktop is None):
    desktop=0
sizes=pygame.display.get_desktop_sizes()
xres=sizes[desktop][0]
yres=sizes[desktop][1]
speed=settings.speed
if(speed is None):
    speed=1.0
num=settings.num
if(num is None):
    num=1
pygame.display.set_mode(size=(xres,yres))
pygame.init()
screen=pygame.display.get_surface()
rect=screen.get_rect()
rects=[rect.scale_by((1/int(num)))]
rects.append(rect)
createdrects=1
while (createdrects<int(num)):
    rect=rects[-1].scale_by((1/(createdrects+1)))
    rects.append(rect)
    createdrects=(createdrects+1)
rects.sort()
surfaces=[]
for r in rects:
    surfaces.append(screen.subsurface(r))
while 1:
    for s in surfaces:
        color=(random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)))
        s.fill(color)
        pygame.display.flip()
        time.sleep((surfaces.index(s)+1)/float(num))
