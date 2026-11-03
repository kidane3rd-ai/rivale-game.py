import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("un.png")
best=pygame.image.load("two.png")
pig=pygame.image.load("trois.png")
poul=pygame.image.load("four.png")
frite=pygame.image.load("cinq.png")
bol=pygame.image.load("propre.png")
font=pygame.font.SysFont("Times New Roman",40)
while(True):
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.quit()
    display_surface.blit(img,(0,0))


    text=font.render("you",True,"Dark Sea Green")
    display_surface.blit(text,(100,300))
    pygame.display.update()
    time.sleep(2)

    display_surface.fill("black") 
    display_surface.blit(best,(0,0))

    text2=font.render("are",True,"white")
    display_surface.blit(text2,(100,300))
    pygame.display.update()
    time.sleep(2)
    
    display_surface.fill("black") 
    display_surface.blit(pig,(0,0))

    text3=font.render("are",True,"black")
    display_surface.blit(text3,(100,300))
    pygame.display.update()
    time.sleep(2)

    

