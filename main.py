import pygame

# Initialize the pygame
pygame.init()
WIDTH = 800
HEIGHT = 600

# Create the screnn
screen = pygame.display.set_mode((WIDTH , HEIGHT))

#Title and Icon
pygame.display.set_caption("Space Invaders by Yves Ronaldo CAZEAU")
icon = pygame.image.load('images/enemy.png')
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()