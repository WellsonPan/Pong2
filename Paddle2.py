import pygame
from pygame.sprite import Sprite

class Paddle2(Sprite):
    def __init__(self, settings, screen, side):
        super(Paddle2, self).__init__()
        self.screen = screen
        self.settings = settings
        self.side = side
        self.rect = pygame.Rect(0, 0, settings.padLength, settings.padWidth)
        self.screenRect = screen.get_rect()

        self.rect.centery = self.screenRect.centery
        if self.side == "left":
            self.rect.left = self.screenRect.left
        elif self.side == "right":
            self.rect.right = self.screenRect.right

        self.center = float(self.rect.centery)

        self.movingUp = False
        self.movingDown = False
        self.hitTop = False
        self.hitBottom = True
        self.color = settings.padColor

    def update(self, ball):
        if self.side == "right":
            if self.movingUp and self.rect.top > self.screenRect.top:
                self.center -= self.settings.padSpeed
            if self.movingDown and self.rect.bottom < self.screenRect.bottom:
                self.center += self.settings.padSpeed
            self.rect.centery = self.center
        elif self.side == "left":
            if not self.hitTop:
                self.center -= self.settings.padSpeed
                self.rect.centery = self.center
                if self.rect.top < self.screenRect.top or self.rect.centery < ball.rect.centery:
                    self.hitTop = True
                    self.hitBottom = False
            elif not self.hitBottom:
                self.center += self.settings.padSpeed
                self.rect.centery = self.center
                if self.rect.bottom > self.screenRect.bottom or self.rect.centery > ball.rect.centery:
                    self.hitTop = False
                    self.hitBottom = True

    def blitPaddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)