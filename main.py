import pygame
import random
from pygame.locals import *
from Ant import Ant

# Define the dimensions of the grid
GRID_WIDTH = 25
GRID_HEIGHT = 20
CELL_SIZE = 40

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the evaporation rate
EVAPORATION_RATE = 0.1

PHEROMONE_INTENSITY = 0.1

# Define the number of ants
NUM_ANTS = 10

# Create the grid as a 2D array
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Initialize Pygame and create the game window
pygame.init()
window = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Ant Colony Game")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a list to hold the ants
ants = []
for _ in range(NUM_ANTS):
    x = random.randint(0, GRID_WIDTH - 1)
    y = random.randint(0, GRID_HEIGHT - 1)
    ant = Ant(x, y, GRID_WIDTH, GRID_HEIGHT)
    ants.append(ant)

# ant = Ant(GRID_WIDTH // 2, GRID_HEIGHT // 2, grid, GRID_WIDTH, GRID_HEIGHT)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    window.fill((0, 128, 0))  # Set background color to green

    # Move the ants
    for ant in ants:
        ant.move(grid)

    # Update pheromone levels
    for ant in ants:
        ant.update_pheromone()
        ant.deposit_pheromone(grid)

    # Evaporate pheromone
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] *= (1 - EVAPORATION_RATE)

    # Render the grid with pheromone trails
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pheromone_level = grid[y][x]
            color_intensity = int(pheromone_level * 255)
            color = (255, 255 - color_intensity, 255 - color_intensity)  # Fade from red to pale red
            print(f"color: {color}")
            pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Render the ants
    for ant in ants:
        pygame.draw.circle(window, BLACK, (ant.x * CELL_SIZE + CELL_SIZE // 2, ant.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(5)

# Quit the game
pygame.quit()