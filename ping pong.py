import pygame
pygame.init()
class player():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img), (self.w,self.h))
        self.img_rect = self.img_new.get_rect()
W,H = (700,450)
name = pygame.display.set_caption("ping_pong")
scr = pygame.display.set_mode((W,H))
bg = pygame.transform.scale(pygame.image.load('eeeeeeeee.jpg'), (W,H))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.blit(bg, (0,0))
    pygame.display.update()


