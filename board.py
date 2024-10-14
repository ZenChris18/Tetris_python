import numpy as np
import pygame
import shape 
from tile import Tile
import random

class Board:
    
    def __init__(self, screen, height=20, width=10):
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
                pygame.draw.rect(self._screen, self._colors[self._matrix[x, y]], rect, 1 if self._matrix[x, y] == 0 else 0)

    def update(self):
        if self._current_tile is None:
            self.create_tile()
        self.draw_tile(self._current_tile)

    def create_tile(self):
        shape = self.get_shape()  # Get a random shape
        color = self.get_color()  # Get a random color
        self._current_tile = Tile(shape, color, random.randint(0, 6))  # Create a Tile instance

    def get_shape(self):
        return self._shapes[random.randint(0, len(self._shapes) - 1)]
    
    def get_color(self):
        return random.randint(1, len(self._colors) - 1)

    def draw_tile(self, tile):
        matrix = tile.get_coordinates()
        for pos in matrix:
            if pos[1] < self._height:
                self._matrix[pos[0], pos[1]] = tile._color
