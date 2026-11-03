import pygame
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH,HEIGHT=900.500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
BULLET_HIT_SOUND=pygame.mixer.Sound("assets/grenade.mp3")
BULLET_FIRE_SOUND=pygame.mixer.Sound("assets/gun.mp3")
HEALTH_font=pygame.font.SysFont("comicsan",40)
WINNER_FONT=pygame.font.SysFont("comicsan",100)
FPS=60
VEL=5
BULLET_VEL=7
MAX_BULLETS=3
SPACESHIP_WIDTH,spaceship_HEIGHT=55,40
YELLOW_SPACESHIP_IMAGE=pygame.image.load("jaune.png")
YELLOW_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(50,40)),90)



RED_SPACESHIP_IMAGE=pygame.image.load("red.png")
RED_SPACESHIP_IMAGE=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(50,40)),270)
SPACE=pygame.image.load("voie lactée.png")
