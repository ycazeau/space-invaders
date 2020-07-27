import pygame

# Initialize the pygame
pygame.init()
WIDTH = 800
HEIGHT = 600

# Create the screnn
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#Caption and Icon
pygame.display.set_caption("Space Invaders by Yves Ronaldo CAZEAU")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/player.png')
playerX = 370
playerY = 500


def player(x , y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))
    playerX +=0.3
    playerY -=0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()