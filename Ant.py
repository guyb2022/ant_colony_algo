import random
import pygame

EVAPORATION_RATE = 0.1
PHEROMONE_INTENSITY = 0.1

# Define the Ant class
class Ant:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.FADE_TIME = 50
        self.pheromone_level = 1.0
        self.pheromone_start_time = pygame.time.get_ticks()

    def check_valid_move(self, x, y):
        if  0 <= x < self.width and 0 <= y < self.height:
            return True
        return False

    def move(self, grid):
        # Get the neighboring cells
        neighbors = [
            (self.x - 1, self.y),  # left
            (self.x + 1, self.y),  # right
            (self.x, self.y - 1),  # up
            (self.x, self.y + 1)   # down
        ]

        # Calculate the sum of pheromone levels in neighboring cells
        sum_pheromone = 0
        valid_neighbors = []
        for neighbor in neighbors:
            x, y = neighbor
            if 0 <= x < self.width and 0 <= y < self.height:
                sum_pheromone += grid[y][x]
                valid_neighbors.append(neighbor)

        if sum_pheromone > 0:
            # Calculate the probabilities of moving to neighboring cells
            probabilities = [grid[y][x] / sum_pheromone if sum_pheromone > 0 else 0 for x, y in valid_neighbors]

            # Choose a random move based on the probabilities
            next_move = random.choice(valid_neighbors)
            self.x, self.y = next_move
        else:
            # If no pheromone trails are present or all moves are invalid, choose a random valid move
            if valid_neighbors:
                self.x, self.y = random.choice(valid_neighbors)


    def deposit_pheromone(self, grid):
        # Deposit pheromone on the current cell
        if self.check_valid_move(self.x, self.y):
            grid[self.y][self.x] += PHEROMONE_INTENSITY

    def update_pheromone(self):
        # Update the pheromone level based on time
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.pheromone_start_time) / 1000  # Convert to seconds
        self.pheromone_level = max(0, 1 - elapsed_time / self.FADE_TIME)