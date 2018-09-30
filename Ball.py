import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    def __init__(self, pongSettings, screen):
        super(Ball, self).__init__()
        self.pongSettings = pongSettings
        self.screen = screen

        self.color = pongSettings.ballColor
        self.rect = pygame.Rect(0, 0, pongSettings.ballWidth, pongSettings.ballHeight)
        self.screenRect = screen.get_rect()
        self.rect.center = self.screenRect.center
        self.rect.centerx = self.screenRect.centerx

        self.hitTop = False
        self.hitBottom = True
        self.hitRight = False
        self.hitLeft = True

        self.xDir = pongSettings.ballDirections[randint(0, 1)]
        self.yDir = pongSettings.ballDirections[randint(0, 1)]

    def drawBall(self):
        pygame.draw.circle(self.screen, self.pongSettings.ballColor, self.rect.center, self.pongSettings.ballWidth)

    def update(self):
        if not self.hitRight:
            self.rect.centerx += (self.pongSettings.ballSpeed * self.xDir)
            # if self.rect.right >= self.screenRect.right:
            #     self.hitRight = True
            #     self.hitLeft = False
        elif not self.hitLeft:
            self.rect.centerx -= (self.pongSettings.ballSpeed * self.xDir)
            # if self.rect.left <= 0:
            #     self.hitRight = False
            #     self.hitLeft = True

        if not self.hitTop:
            self.rect.centery -= (self.pongSettings.ballSpeed * self.yDir)
            # if self.rect.top <= self.screenRect.top:
            #     self.hitTop = True
            #     self.hitBottom = False
        elif not self.hitBottom:
            self.rect.centery += (self.pongSettings.ballSpeed * self.yDir)
            # if self.rect.bottom >= self.screenRect.bottom:
            #     self.hitTop = False
            #     self.hitBottom = True

    def reset(self):
        self.rect.center = self.screenRect.center