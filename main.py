import pygame
from pygame.constants import QUIT


pygame.init()


FPS = pygame.time.Clock()

HEIGHT = 915
WIDTH = 1400
backGround = pygame.image.load("src/backGround.jpg")

mainDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
playerSize = (20, 20)

player = pygame.Surface(playerSize)
player.fill(WHITE)
playerRect = player.get_rect()
playerSpeed = [1, 1]

playing = True
while playing:
    FPS.tick(400)
    for e in pygame.event.get():
        if e.type == QUIT:
            playing = False

    if playerRect.bottom >= HEIGHT:
        playerSpeed[1] = -playerSpeed[1]
    if playerRect.right >= WIDTH:
        playerSpeed[0] = -playerSpeed[0]
    if playerRect.top < 0:
        playerSpeed[1] = -playerSpeed[1]
    if playerRect.left < 0:
        playerSpeed[0] = -playerSpeed[0]
    # print(playerRect.top)

    mainDisplay.blit(backGround, (0, 0))
    mainDisplay.blit(player, playerRect)

    playerRect = playerRect.move(playerSpeed)

    pygame.display.flip()
