import pygame
import random
import os
from time import sleep
import pygame.freetype
pygame.init()

HEIGHT = 500
WIDTH= 500
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255 , 0,0)




Yes = pygame.image.load("Yes.png")
No = pygame.image.load("No.png")
button1 = pygame.Rect(100 , 350 , 150 , 100)
button2 = pygame.Rect(300 , 350 , 150 , 100)
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Are You Stupid")
screen.fill(WHITE)

screen.blit(Yes, (300, 350, 150, 100))
screen.blit(No,(100,350, 150, 100))
button1 = pygame.Rect(100, 350, 150, 100)
button2 = pygame.Rect(300, 350, 150, 100)

#run = True

my_font = pygame.font.SysFont("ATypewriterForMe.ttf", 100)
font = pygame.font.SysFont("ATypewriterForMe.ttf", 70)
text_surface = font.render('I thought so ', False, (BLACK))
question  = my_font.render("Are You Stupid?",False,(BLACK))
screen.blit(question, (5, 100))
pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    r = random.randint(1, 350)
    R = random.randint(1, 400)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    clicked = False

    POS = pygame.mouse.get_pos()
    if button1.collidepoint(POS):
           if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
               screen.fill(WHITE)
               screen.blit(question, (5, 100))
               clicked = True
               button1 = pygame.Rect(r, R, 150, 100)
               screen.blit(No,(r,R, 150, 100))
               screen.blit(Yes, (300, 350, 150, 100))
               pygame.display.update()
    if button2.collidepoint(POS):
        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            screen.fill(WHITE)
            screen.blit(text_surface, (85,250))
            pygame.display.update()
            pygame.QUIT
