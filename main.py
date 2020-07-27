import pygame
import random

# Initialize the pygame
pygame.init()
screen_size = WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 64

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Caption and Icon
pygame.display.set_caption("Space Invaders by Yves Ronaldo CAZEAU")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/player.png')
playerX = (WIDTH / 2) - (PLAYER_SIZE / 2)
playerY = 500
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('images/enemy.png')
enemyX = random.randint(0, WIDTH)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Check Key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Define Boundaries for the player so it's doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= WIDTH - PLAYER_SIZE:
        playerX = WIDTH - PLAYER_SIZE

    # Define Boundaries for the enemy so it's doesn't go out of bounds
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= WIDTH - PLAYER_SIZE:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
