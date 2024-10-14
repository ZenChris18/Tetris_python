import numpy as np


class Tile:
    def __init__(self, shape, color, pos_x=5, pos_y=0 , rotation=0):
        self._shape = shape
        self._rotation = rotation
        self._color = color
        self._position = np.array([pos_x, pos_y])

    def render(self, board):
        matrix = self.get_coordinates()
        board.draw_tile()

    def get_coordinates(self):
        return self._shape.get_matrix_with_offset(self._rotation, self._position)