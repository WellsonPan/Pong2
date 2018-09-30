import sys
import pygame
from Ball import Ball
from Paddle import Paddle
from Paddle2 import Paddle2

def check_play_button(pongSettings, play_button, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not pongSettings.gameActive:
        pygame.mouse.set_visible(False)
        pongSettings.gameActive = True
        sb.prep_score()

def checkEvents(pongSettings, paddle, paddle3, paddle5, play_button, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(pongSettings, play_button, mouse_x, mouse_y, sb)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle.movingRight = True
                paddle5.movingRight = True
            elif event.key == pygame.K_LEFT:
                paddle.movingLeft = True
                paddle5.movingLeft = True
            elif event.key == pygame.K_UP:
                paddle3.movingUp = True
            elif event.key == pygame.K_DOWN:
                paddle3.movingDown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle.movingRight = False
                paddle5.movingRight = False
            elif event.key == pygame.K_LEFT:
                paddle.movingLeft = False
                paddle5.movingLeft = False
            elif event.key == pygame.K_UP:
                paddle3.movingUp = False
            elif event.key == pygame.K_DOWN:
                paddle3.movingDown = False

def checkPaddleBallCollision(ball, paddleTopBottom, paddleLeftRight, pongSettings):
    if pygame.sprite.spritecollideany(ball, paddleTopBottom) and ball.yDir == 1:
        ball.yDir = -1
        pongSettings.speedUp()
    elif pygame.sprite.spritecollideany(ball, paddleTopBottom) and ball.yDir == -1:
        ball.yDir = 1
        pongSettings.speedUp()

    if pygame.sprite.spritecollideany(ball, paddleLeftRight) and ball.xDir == 1:
        ball.xDir = -1
        pongSettings.speedUp()
    elif pygame.sprite.spritecollideany(ball, paddleLeftRight) and ball.xDir == -1:
        ball.xDir = 1
        pongSettings.speedUp()

def checkOutOfBounds(ball, pongSettings, screen, sb):
    screenRect = screen.get_rect()
    if ball.rect.centerx < screenRect.centerx:
        if ball.rect.centerx < 0:
            pongSettings.playerScored()
            sb.prep_score()
            pongSettings.reset()
            ball.reset()
        elif ball.rect.centery < 0:
            pongSettings.playerScored()
            sb.prep_score()
            pongSettings.reset()
            ball.reset()
        elif ball.rect.centery > screenRect.bottom:
            pongSettings.playerScored()
            sb.prep_score()
            pongSettings.reset()
            ball.reset()
    elif ball.rect.centerx > screenRect.centerx:
        if ball.rect.centerx > screenRect.right:
            pongSettings.AIScored()
            sb.prep_score()
            pongSettings.reset()
            ball.reset()
        elif ball.rect.centery < 0:
            pongSettings.AIScored()
            sb.prep_score()
            pongSettings.reset()
            ball.reset()
        elif ball.rect.centery > screenRect.bottom:
            pongSettings.AIScored()
            sb.prep_score()
            pongSettings.reset()
            ball.reset()

def checkScore(pongSettings):
    if pongSettings.playerScore >= 7 or pongSettings.AIScore >= 7:
        pongSettings.reset_score()
        pongSettings.gameActive = False
        pygame.mouse.set_visible(True)

def updateScreen(pongSettings, screen, paddle, paddle2, paddle3, paddle4, paddle5, paddle6, ball, divide, sb):
    screen.fill(pongSettings.backgroundColor)
    ball.drawBall()
    divide.drawDivider()
    paddle.blitPaddle()
    paddle2.blitPaddle()
    paddle3.blitPaddle()
    paddle4.blitPaddle()
    paddle5.blitPaddle()
    paddle6.blitPaddle()
    sb.show_score()
    pygame.display.flip()

def startGame(play_button, startScreen):
    startScreen.printStart()
    play_button.draw_button()
    pygame.display.flip()
