import pygame

class Divider():
    def __init__(self, pongSettings, screen):
        self.pongSettings = pongSettings
        self.screen = screen

        self.rect = pygame.Rect(0, 0, pongSettings.dividerWidth, pongSettings.dividerHeight)
        self.screenRect = screen.get_rect()
        self.color = self.pongSettings.dividerColor

        self.rect.centerx = self.screenRect.centerx

    def drawDivider(self):
        pygame.draw.rect(self.screen, self.color, self.rect)