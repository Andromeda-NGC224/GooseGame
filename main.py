import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 915
WIDTH = 1400
PURPLE = (118, 43, 194)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 216, 89)

backGround = pygame.image.load("src/backGround.jpg")
mainDisplay = pygame.display.set_mode((WIDTH, HEIGHT))


playerSize = (20, 20)
player = pygame.Surface(playerSize)
playerRect = player.get_rect()
player.fill(PURPLE)
playerMoveDown = [0, 2]
playerMoveUp = [0, -2]
playerMoveLeft = [-2, 0]
playerMoveRight = [2, 0]


def createEnemy():
    enemySize = (30, 30)
    enemy = pygame.Surface(enemySize)
    enemy.fill(RED)
    enemyRect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemySize)
    enemyMove = [random.randint(-5, -1), 0]
    return [enemy, enemyRect, enemyMove]


enemies = []

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 500)


def createBonus():
    bonusSize = (20, 20)
    bonus = pygame.Surface(bonusSize)
    bonus.fill(GOLD)
    bonusRect = pygame.Rect(random.randint(0, WIDTH), 0, *bonusSize)
    bonusMove = [0, 1]
    return [bonus, bonusRect, bonusMove]


bonuses = []

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 3000)


playing = True

while playing:
    mainDisplay.blit(backGround, (0, 0))
    FPS.tick(400)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(createEnemy())
        if event.type == CREATE_BONUS:
            bonuses.append(createBonus())

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_BONUS:
            bonuses.append(createBonus())

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and playerRect.bottom < HEIGHT:
        playerRect = playerRect.move(playerMoveDown)

    if keys[K_UP] and playerRect.top > 0:
        playerRect = playerRect.move(playerMoveUp)

    if keys[K_LEFT] and playerRect.left > 0:
        playerRect = playerRect.move(playerMoveLeft)

    if keys[K_RIGHT] and playerRect.right < WIDTH:
        playerRect = playerRect.move(playerMoveRight)

    if keys[K_s] and playerRect.bottom < HEIGHT:
        playerRect = playerRect.move(playerMoveDown)

    if keys[K_w] and playerRect.top > 0:
        playerRect = playerRect.move(playerMoveUp)

    if keys[K_a] and playerRect.left > 0:
        playerRect = playerRect.move(playerMoveLeft)

    if keys[K_d] and playerRect.right < WIDTH:
        playerRect = playerRect.move(playerMoveRight)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        mainDisplay.blit(enemy[0], enemy[1])
        print(len(enemies))

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        mainDisplay.blit(bonus[0], bonus[1])

    mainDisplay.blit(player, playerRect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
