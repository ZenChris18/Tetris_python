import numpy as np


class Shape:
    def __init__(self, rotations):
        self.rotations = rotations
        self.rotations_count = len(rotations)

    def get_matrix_with_offset(self, rotation, offset):
        return offset + self.rotations[rotation]


def generate_shapes():
    # for the shape I
    shape_i_rotate1 = np.array([[1, 0], [1, 1], [1, 2], [1, 3]], np.int32)
    shape_i_rotate2 = np.array([[0, 1], [1, 1], [2, 1], [3, 1]], np.int32)
    shape_i = Shape(np.array([shape_i_rotate1, shape_i_rotate2]))

    # for the shape L
    shape_l_rotate1 = np.array([[1, 0], [1, 1], [1, 2], [2, 2]], np.int32)
    shape_l_rotate2 = np.array([[0, 2], [1, 2], [2, 2], [2, 1]], np.int32)
    shape_l_rotate3 = np.array([[1, 0], [2, 0], [2, 1], [2, 2]], np.int32)
    shape_l_rotate4 = np.array([[0, 3], [0, 2], [1, 2], [2, 2]], np.int32)
    shape_l = Shape(np.array([shape_l_rotate1, shape_l_rotate2, shape_l_rotate3, shape_l_rotate4]))

    # for the shape J
    shape_j_rotate1 = np.array([[2, 0], [2, 1], [2, 2], [1, 2]], np.int32)
    shape_j_rotate2 = np.array([[0, 1], [1, 1], [2, 1], [2, 2]], np.int32)
    shape_j_rotate3 = np.array([[3, 0], [2, 0], [2, 1], [2, 2]], np.int32)
    shape_j_rotate4 = np.array([[0, 1], [0, 2], [1, 2], [2, 2]], np.int32)
    shape_j = Shape(np.array([shape_j_rotate1, shape_j_rotate2, shape_j_rotate3, shape_j_rotate4]))

    # for the shape S
    shape_s_rotate1 = np.array([[0, 2], [1, 2], [1, 1], [2, 1]], np.int32)
    shape_s_rotate2 = np.array([[1, 0], [1, 1], [2, 1], [2, 2]], np.int32)
    shape_s = Shape(np.array([shape_s_rotate1, shape_s_rotate2]))

    # for the shape Z
    shape_z_rotate1 = np.array([[0, 1], [1, 1], [1, 2], [2, 2]], np.int32)
    shape_z_rotate2 = np.array([[2, 0], [2, 1], [1, 1], [1, 2]], np.int32)
    shape_z = Shape(np.array([shape_z_rotate1, shape_z_rotate2]))

    # for the shape T
    shape_t_rotate1 = np.array([[0, 2], [1, 2], [2, 2], [1, 1]], np.int32)
    shape_t_rotate2 = np.array([[2, 0], [2, 1], [2, 2], [1, 1]], np.int32)
    shape_t_rotate3 = np.array([[0, 1], [1, 1], [2, 1], [1, 2]], np.int32)
    shape_t_rotate4 = np.array([[1, 0], [1, 1], [1, 2], [2, 1]], np.int32)
    shape_t = Shape(np.array([shape_t_rotate1, shape_t_rotate2, shape_t_rotate3, shape_t_rotate4]))

    shape_o_rotate1 = np.array([[1, 1], [1, 2], [2, 1], [2, 2]], np.int32)
    shape_o = Shape(np.array([shape_o_rotate1]))

    return list([shape_i, shape_l, shape_j, shape_s, shape_z, shape_t, shape_o])


def generate_colours():
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    YELLOW = [204, 204, 0]
    BLUE = [0, 0, 255]
    OLIVE = [128, 128, 0]
    ORANGE = [255, 165, 0]
    WHITE = [125, 125, 125]
    return list([WHITE, BLUE, RED, GREEN, ORANGE, GREEN, YELLOW, OLIVE])