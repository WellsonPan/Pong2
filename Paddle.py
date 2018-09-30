import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, settings, screen, control, side):
        super(Paddle, self).__init__()
        self.screen = screen
        self.settings = settings
        self.control = control
        self.side = side
        self.rect = pygame.Rect(0, 0, settings.padWidth, settings.padLength)
        self.screenRect = screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        if self.control == "AI":
            if self.side == "bottom":
                self.rect.bottom = self.screenRect.bottom
            elif self.side == "top":
                self.rect.top = self.screenRect.top
            self.rect.centerx = self.screenRect.centerx / 4
        elif self.control == "player":
            if self.side == "bottom":
                self.rect.bottom = self.screenRect.bottom
            elif self.side == "top":
                self.rect.top = self.screenRect.top
            self.rect.centerx = (self.screenRect.centerx * 3) / 2

        self.center = float(self.rect.centerx)

        self.movingRight = False
        self.movingLeft = False
        self.hitRight = False
        self.hitLeft = True
        self.color = settings.padColor

    def update(self, ball):
        if self.control == "player":
            if self.movingRight and self.rect.right < self.screenRect.right:
                self.center += self.settings.padSpeed
            if self.movingLeft and self.rect.left >= self.screenRect.centerx:
                self.center -= self.settings.padSpeed

            self.rect.centerx = self.center
        elif self.control == "AI":
            if not self.hitRight and ball.rect.centerx < self.screenRect.centerx:
                self.center += self.settings.padSpeed
                self.rect.centerx = self.center
                if self.rect.right > self.screenRect.right or self.rect.centerx > ball.rect.centerx or (self.rect.x + self.settings.padWidth) >= self.screenRect.centerx:
                    self.hitRight = True
                    self.hitLeft = False
            elif not self.hitLeft:
                self.center -= self.settings.padSpeed
                self.rect.centerx = self.center
                if self.rect.left < 0 or self.rect.centerx < ball.rect.centerx:
                    self.hitRight = False
                    self.hitLeft = True


    def blitPaddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)





