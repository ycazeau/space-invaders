import math

import pygame
import random

# Initialize the pygame
pygame.init()
screen_size = WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 64

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Add background
background = pygame.image.load('images/background.png')

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 100

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, WIDTH - 65))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(30)

# Bullet
# Ready - You can't see the nullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Check Key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - 5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= WIDTH - PLAYER_SIZE:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Detect Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 400
            bullet_state = "ready"
            score += 5
            print(score)
            enemyX[i] = random.randint(0, WIDTH - 65)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    pygame.display.update()
