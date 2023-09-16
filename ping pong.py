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
        self.img_rect = self.img_new.get_rect()(center = (self.x, self.y))
player = Player(50,190,30,175,'platforma.png')
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
    scr.blit(player.img_new, (player.img_rect.x,player.img_rect.y))
    pygame.display.update()


