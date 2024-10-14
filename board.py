import numpy as np
import pygame
import shape 

class Board:
    
    def __init__(self, screen, height = 20, width= 10):
        self._height = height
        self._width = width
        self._screen = screen
        self._matrix = np.zeros([width, height], dtype=int)
        self._current_tile = None
        self._score = 0
        self._colors = shape.generate_colours()
        self._shapes = shape.generate_shapes()

    def draw(self):
        blockSize = 35 
        x_offset = 100
        y_offset = 50
        for x in range(0, self._width):
            for y in range(0, self._height):
                rect = pygame.Rect(x_offset + x * blockSize, y_offset + y * blockSize, blockSize, blockSize)
                pygame.draw.rect(self._screen, self._colors[self._matrix[x, y]], rect)