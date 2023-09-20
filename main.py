import pygame
from pygame.locals import *
from sys import exit
import random
# import os, sys
# from fcntl import ioctl

pygame.init()

# RD_SWITCHES   = 24929
# RD_PBUTTONS   = 24930
# WR_L_DISPLAY  = 24931
# WR_R_DISPLAY  = 24932
# WR_RED_LEDS   = 24933
# WR_GREEN_LEDS = 24934
# DATA = 0
# fd = os.open(sys.argv[1], os.O_RDWR)
# button = 0


k = 1
i = 0
score = 0
hearts = 3
width = 700
height = 466
i_sugar = random.randint(0,3)
i_mug = 0
positions_sugar = 63, 238, 415, 605
v_sugar = 10 + k * 4
X_sugar = positions_sugar[i_sugar]
Y_sugar = 40
positions_mug = 38, 213, 390, 585
X_mug = positions_mug[i_mug]
Y_splash = 338

MOVE_MUG = True
END_GAME = False
BLACK = (0, 0, 0)


Font1 = pygame.font.SysFont('franklingothicmedium', 25, True, False)
Font2 = pygame.font.SysFont('franklingothicmedium', 25, False, True)
Font3 = pygame.font.SysFont('franklingothicmedium', 50, False, True)
screen = pygame.display.set_mode((width, height))
sugar = pygame.image.load('sugar.png')
sugar = pygame.transform.scale(sugar, (50, 50))
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background, (700, 466))
mug = pygame.image.load('mug.png')
heart = pygame.image.load(('heart.png'))
heart = pygame.transform.scale(heart, (50, 50))
dead_heart = pygame.image.load('dead_heart.png')
dead_heart = pygame.transform.scale(dead_heart, (50, 50))
mug = pygame.transform.scale(mug, (100, 100))


class Splash(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Splash0.png'))
        self.sprites.append(pygame.image.load('Splash1.png'))
        self.sprites.append(pygame.image.load('Splash2.png'))
        self.sprites.append(pygame.image.load('Splash3.png'))
        self.sprites.append(pygame.image.load('Splash4.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()

        self.animate = False

    def splash(self):
        self.animate = True

    def update(self, X_mug):
        self.rect.topleft = X_mug, Y_splash
        if self.animate == True:
            if self.atual == 0:
                self.atual = self.atual + 1
            else:
                self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animate = False
            self.image = self.sprites[int(self.atual)]

Game_Sprites = pygame.sprite.Group()
Splash_ = Splash()
Game_Sprites.add(Splash_)
clock = pygame.time.Clock()

screen.fill(BLACK)


while True:
    clock.tick(30)
    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    screen.blit(sugar, (X_sugar, Y_sugar))
    screen.blit(mug, (X_mug, 380))
    if hearts == 1:
        screen.blit(dead_heart, (550, 20))
        screen.blit(dead_heart, (600, 20))
        screen.blit(heart, (650, 20))
    if hearts == 2:
        screen.blit(dead_heart, (550, 20))
        screen.blit(heart, (600, 20))
        screen.blit(heart, (650, 20))
    if hearts == 3:
        screen.blit(heart, (550, 20))
        screen.blit(heart, (600, 20))
        screen.blit(heart, (650, 20))

    #X_mug = positions_mug[button]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_LEFT]:
            i_mug = i_mug - 1
            if i_mug < 0:
                i_mug = 3
            X_mug = positions_mug[i_mug]
        if pygame.key.get_pressed()[K_RIGHT]:
            i_mug = i_mug + 1
            if i_mug > 3:
                i_mug = 0
            X_mug = positions_mug[i_mug]


    if END_GAME == False:
        Y_sugar = Y_sugar + v_sugar
        if Y_sugar >= 380:
            Y_sugar = 40
            i_sugar = random.randint(0, 3)
            hearts = hearts - 1
            screen.blit(dead_heart, (600, 20))
            X_sugar = positions_sugar[i_sugar]

    if hearts == 0 :
        END_GAME = True
        # DATA = 0xFFFFFFFF
        # ioctl(fd, WR_RED_LEDS)
        # retval = os.write(fd, DATA.to_bytes(4, 'little'))
        # #print("wrote %d bytes" % retval)


    if score == 15:
        END_GAME = True
        screen.blit(dead_heart, (550, 20))
        screen.blit(dead_heart, (600, 20))
        screen.blit(dead_heart, (650, 20))
        # DATA = 0xFFFFFFFF
        # ioctl(fd, WR_GREEN_LEDS)
        # retval = os.write(fd, DATA.to_bytes(4, 'little'))
        # # print("wrote %d bytes" % retval)

        exit()

    if 360 <= Y_sugar <= 370 and i_mug == i_sugar:
        score = score + 1
        Splash_.splash()
        Game_Sprites.draw(screen)
        Game_Sprites.update(X_mug)
        Y_sugar = 40
        i_sugar = random.randint(0, 3)
        X_sugar = positions_sugar[i_sugar]

    Game_Sprites.draw(screen)
    Game_Sprites.update(X_mug)
    pygame.display.flip()



