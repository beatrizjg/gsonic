import retro
import os
import pygame
from pygame.locals import *


env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
clock = pygame.time.Clock()
obs = env.reset()
pygame.init()
ven = pygame.display.set_mode((400,200))

done = False
info = {'level_end_bonus': 0}
def key_action():
    keys=pygame.key.get_pressed()
    key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if keys[K_LEFT]:
        key[6] = 1
    if keys[K_UP]:
        key[0] = 1
    if keys[K_RIGHT]:
        key[7] = 1
    if keys[K_DOWN]:
        key[5] = 1
    return key

archivo = open("sonyA.csv","a")
while info['level_end_bonus'] != 1:
 
    ven = pygame.display.set_mode((400,200))
    screen = pygame.image.frombuffer(obs.tostring(), obs.shape[1::-1], 'RGB')
    screen= pygame.transform.scale(screen, (400,200))
    ven.blit(screen,(0,0))
    pygame.display.flip()

    action = key_action()
    obs, rew, done, info = env.step(action)
    archivo.write(str(info))
    archivo.write(";")
    archivo.write(str(action))
    archivo.write(";")
    archivo.write(str(rew))
    archivo.write(";")
    archivo.write("\n")
clock.tick(5) 
archivo.close()
