import pygame

# Initialize the pygame
pygame.init()

# Create the screnn
screen = pygame.display.set_mode((600 , 400))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False