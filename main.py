import pygame

# Initialize the pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 64

# Create the screnn
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#Caption and Icon
pygame.display.set_caption("Space Invaders by Yves Ronaldo CAZEAU")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/player.png')
playerX = (WIDTH / 2 )- (PLAYER_SIZE / 2)
playerY = 500
playerX_change = 0


def player(x , y):
    screen.blit(playerImg, (x, y))

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

    playerX += playerX_change

    if playerX <= 0:
        playerX =0
    elif playerX >= WIDTH - PLAYER_SIZE:
        playerX = WIDTH - PLAYER_SIZE


    player(playerX, playerY)
    pygame.display.update()