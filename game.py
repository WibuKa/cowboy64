import pygame
pygame.init

from scripts.test import _x

print(_x)
ml_size = 8
icon = pygame.image.load(r'D:\pygame\project_A\art\icon_game.png')
cowboy_load = pygame.image.load(r'D:\pygame\project_A\art\cowboy.png')
BG_load = pygame.image.load(r'D:\pygame\project_A\art\BG.png')

cowboy = pygame.transform.scale_by(cowboy_load,ml_size)
Background = pygame.transform.scale_by(BG_load,ml_size)

pygame.display.set_icon(icon)
pygame.display.set_caption("project A")
screen = pygame.display.set_mode((64*ml_size,64*ml_size))

cowboy_x,cowboy_y = 24*ml_size,49*ml_size

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    BG_obj = screen.blit(Background,(0,0))
    cowboy_obj = screen.blit(cowboy,(cowboy_x,cowboy_y))
    pygame.display.update()