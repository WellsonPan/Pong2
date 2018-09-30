import pygame
from pygame.sprite import Group
from settings import Settings
from Paddle import Paddle
from Paddle2 import Paddle2
import gameFunctions as gf
from Ball import Ball
from Divider import Divider
from Button import Button
from Scoreboard import Scoreboard
from Start import Start


def runGame():
    pygame.init()
    pongSettings = Settings()
    screen = pygame.display.set_mode((pongSettings.screenWidth, pongSettings.screenHeight))
    pygame.display.set_caption("Pong 2")

    paddleTopBottom = Group()
    paddleLeftRight = Group()

    paddle = Paddle(pongSettings, screen, "player", "bottom")
    paddle3 = Paddle2(pongSettings, screen, "right")
    paddle5 = Paddle(pongSettings, screen, "player", "top")

    paddle2 = Paddle2(pongSettings, screen, "left")
    paddle4 = Paddle(pongSettings, screen, "AI", "top")
    paddle6 = Paddle(pongSettings, screen, "AI", "bottom")

    paddleTopBottom.add(paddle, paddle4, paddle5, paddle6)
    paddleLeftRight.add(paddle2, paddle3)
    ball = Ball(pongSettings, screen)
    divide = Divider(pongSettings, screen)

    play_button = Button(pongSettings, screen, "Play")
    sb = Scoreboard(pongSettings, screen)
    startScreen = Start(pongSettings, screen)

    while True:
        gf.checkEvents(pongSettings, paddle, paddle3, paddle5, play_button, sb)
        if pongSettings.gameActive:
            gf.checkPaddleBallCollision(ball, paddleTopBottom, paddleLeftRight, pongSettings)
            gf.checkOutOfBounds(ball, pongSettings, screen, sb)
            paddle.update(ball)
            paddle2.update(ball)
            paddle3.update(ball)
            paddle4.update(ball)
            paddle5.update(ball)
            paddle6.update(ball)
            ball.update()
            gf.updateScreen(pongSettings, screen, paddle, paddle2, paddle3, paddle4, paddle5, paddle6, ball, divide, sb)
        else:
            gf.startGame(play_button, startScreen)

runGame()
