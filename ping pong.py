import pygame
pygame.init()
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


