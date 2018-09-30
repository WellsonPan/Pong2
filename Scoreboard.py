import pygame.font
from pygame.sprite import Group

class Scoreboard():
    def __init__(self, pongSettings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pongSettings = pongSettings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        rounded_score_AI = int(self.pongSettings.AIScore)
        rounded_score_player = int(self.pongSettings.playerScore)
        score_str_AI = "{:,}".format(rounded_score_AI)
        score_str_player = "{:,}".format(rounded_score_player)
        self.score_image_AI = self.font.render(score_str_AI, True, self.text_color, self.pongSettings.backgroundColor)
        self.score_image_player = self.font.render(score_str_player, True, self.text_color, self.pongSettings.backgroundColor)

        self.score_rect_AI = self.score_image_AI.get_rect()
        self.score_rect_AI.right = self.screen_rect.centerx - 20
        self.score_rect_AI.top = 20

        self.score_rect_player = self.score_image_player.get_rect()
        self.score_rect_player.left = self.screen_rect.centerx + 20
        self.score_rect_player.top = 20

    def show_score(self):
        self.screen.blit(self.score_image_AI, self.score_rect_AI)
        self.screen.blit(self.score_image_player, self.score_rect_player)
