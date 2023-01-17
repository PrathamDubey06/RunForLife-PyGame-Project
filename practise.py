import time
import pygame
pygame.init()

# Creating Window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First PyGame")

# Game Specific Variables
exit_game = False
game_over = False

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You pressed right arrow key")

pygame.quit()
quit()
