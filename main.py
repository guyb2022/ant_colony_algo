import pygame
import random
from pygame.locals import *
from Ants import Ant

# Define the dimensions of the grid
GRID_WIDTH = 40
GRID_HEIGHT = 25
CELL_SIZE = 20

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the fade time for the pheromone trail
FADE_TIME = 5000  # In milliseconds

# Define the number of ants
NUM_ANTS = 50

# Initialize Pygame and create the game window
pygame.init()
window = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Ant Colony Simulation")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a list to hold the ants
ants = []

# Create the grid as a 2D array
grid = [[0.0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Initialize the ants and add them to the list
for _ in range(NUM_ANTS):
    x = random.randint(0, GRID_WIDTH - 1)
    y = random.randint(0, GRID_HEIGHT - 1)
    ant = Ant(x, y, FADE_TIME)
    ants.append(ant)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    window.fill(WHITE)

    # Move the ants
    for ant in ants:
        ant.move(grid)

    # Update the pheromone levels
    for ant in ants:
        ant.update_pheromone()
        ant.deposit_pheromone(grid)

    # Render the grid with pheromone trails
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pheromone_level = grid[y][x]
            color_intensity = int(pheromone_level * 255)
            color = (255, 255 - color_intensity, 255 - color_intensity)  # Fade from red to white
            pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Render the ants
    for ant in ants:
        pygame.draw.circle(window, BLACK, (ant.x * CELL_SIZE + CELL_SIZE // 2, ant.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(10)

# Quit the game
pygame.quit()
