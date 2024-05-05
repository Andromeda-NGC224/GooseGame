import pygame
import os
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
FONT = pygame.font.SysFont("Verdena", 40)
IMG_PATH = "Player"
PLAYER_IMG = os.listdir(IMG_PATH)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 200)

imgIndex = 0

backGround = pygame.transform.scale(
    pygame.image.load("src/backGround.png"), (WIDTH, HEIGHT)
)
backGroundX1 = 0
backGroundX2 = backGround.get_width()
backGroundMove = 4

mainDisplay = pygame.display.set_mode((WIDTH, HEIGHT))


playerSize = (170, 100)
player = pygame.image.load("Player/1-1.png").convert_alpha()
# pygame.Surface(playerSize)
playerRect = player.get_rect()
playerMoveDown = [0, 12]
playerMoveUp = [0, -12]
playerMoveLeft = [-12, 0]
playerMoveRight = [12, 0]


def createEnemy():
    enemySize = (30, 30)
    enemy = pygame.image.load("src/enemy.png").convert_alpha()
    enemy = pygame.transform.scale(
        enemy, (int(enemy.get_width() / 1.5), int(enemy.get_height() / 1.5))
    )
    enemyRect = pygame.Rect(WIDTH, random.randint(10, HEIGHT - 10), *enemySize)
    enemyMove = [random.randint(-18, -12), 0]
    return [enemy, enemyRect, enemyMove]


enemies = []

CREATE_ENEMY = pygame.USEREVENT + 12
pygame.time.set_timer(CREATE_ENEMY, 500)


def createBonus():
    bonusSize = (100, 100)
    bonus = pygame.image.load("src/goldBag.png").convert_alpha()
    bonus = pygame.transform.scale(
        bonus, (int(bonus.get_width() / 10), int(bonus.get_height() / 10))
    )
    bonusRect = pygame.Rect(random.randint(10, WIDTH - 10), 0, *bonusSize)
    bonusMove = [0, random.randint(7, 10)]
    return [bonus, bonusRect, bonusMove]


bonuses = []

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 3000)


score = 0

playing = True

while playing:
    FPS.tick(240)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(createEnemy())
        if event.type == CREATE_BONUS:
            bonuses.append(createBonus())
        if event.type == CHANGE_IMG:
            player = pygame.image.load(os.path.join(IMG_PATH, PLAYER_IMG[imgIndex]))
            imgIndex += 1
            if imgIndex >= len(PLAYER_IMG):
                imgIndex = 0

    backGroundX1 -= backGroundMove
    backGroundX2 -= backGroundMove

    if backGroundX1 < -backGround.get_width():
        backGroundX1 = backGround.get_width()
    if backGroundX2 < -backGround.get_width():
        backGroundX2 = backGround.get_width()

    mainDisplay.blit(backGround, (backGroundX1, 0))
    mainDisplay.blit(backGround, (backGroundX2, 0))

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

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        mainDisplay.blit(bonus[0], bonus[1])

    mainDisplay.blit(FONT.render(str(score), True, BLACK), (WIDTH - 100, 40))
    mainDisplay.blit(player, playerRect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if playerRect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))

        if playerRect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
