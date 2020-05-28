import numpy as np
from numpy import *


class Edging:
    """Edging inversion matrix methood"""

    def __init__(self, Matrix):
        self.matrix = array(Matrix)
        self.__matrix_length = len(Matrix)

    @property
    def matr_len(self):
        return self.__matrix_length

    def check_on_zero(self):
        for row in range(self.matr_len):
            for column in range(self.matr_len):
                if row == column:
                    if self.matrix[row][column] == 0:
                        return False
        try:
            return self.ending()
        except Exception:
            return False

    def ending(self):
        self.row = []
        self.column = []

        M = 1 / self.matrix[0][0]

        for row in range(1, self.matr_len):
            for column in range(row):
                self.row.append(self.matrix[row][column])
                self.column.append(self.matrix[column][row])

            diagonal_elem = self.matrix[row][column + 1]

            try:
                A = 1 / (diagonal_elem - (array(self.row).dot(M)
                                          ).dot(array(self.column)))
                R = (-A) * (array(M).dot(array(self.column)))
                Q = (-A) * (array(self.row).dot(array(M)))
                B = M - (array(M).dot(array(self.column))).dot(Q)
            except Exception:
                return False

            if row == 1:
                B = array([B])
                A = array([A])
                ROW1 = column_stack((B, R))
                ROW2 = column_stack((Q, A))
                M = row_stack((ROW1, ROW2))

            else:
                B = array(
                    M - ((matrix(M.dot(self.column)).T)).dot(matrix(Q)))
                R = list(R)
                R.append(A)
                R = array(R)
                B = row_stack((B, Q))
                M = column_stack((B, R))

            self.row.clear()
            self.column.clear()

        return M


class Blockwise:
    """Blockwise inversion matrix methood"""

    def __init__(self, Matrix):
        self.matrix = Matrix
        self.__matrix_length = len(Matrix)
        self.reverse = 0

    @property
    def matr_len(self):
        return self.__matrix_length

    def determinant(self, matr):
        return linalg.det(matrix(matr))

    def reverse_two(self, matr):
        try:
            matr[0][0], matr[1][1] = matr[1][1], matr[0][0]
            matr[0][1] = -matr[0][1]
            matr[1][0] = -matr[1][0]
            return (1 / (self.determinant(matr))) * matrix(matr)
        except Exception:
            return False

    """partiting the matrix on the blocks and return the elements sequence"""

    def on_blocks(self, matr, size):
        first = []
        for row in range(int(size / 2)):
            for column in range(int(size / 2)):
                first.append(matr[row][column])

        second = []
        for row in range(int(size / 2)):
            for column in range(int(size / 2), size):
                second.append(matr[row][column])

        third = []
        for row in range(int(size / 2), size):
            for column in range(int(size / 2)):
                third.append(matr[row][column])

        fourth = []
        for row in range(int(size / 2), size):
            for column in range(int(size / 2), size):
                fourth.append(matr[row][column])

        return first, second, third, fourth

    """functions gets suquence and return the matrix"""

    def sequence_to_matr(self, seq, size):
        get_matr = []
        for row in range(int(size / 2)):
            get_matr.append([])
            for column in range(int(size / 2)):
                get_matr[row].append(seq[column])
            seq = seq[column + 1:]
        return get_matr

    def partiting(self, matr):
        section_A = self.sequence_to_matr(
            self.on_blocks(matr, len(matr))[0], len(matr))
        section_B = self.sequence_to_matr(
            self.on_blocks(matr, len(matr))[1], len(matr))
        section_C = self.sequence_to_matr(
            self.on_blocks(matr, len(matr))[2], len(matr))
        section_D = self.sequence_to_matr(
            self.on_blocks(matr, len(matr))[3], len(matr))
        return section_A, section_B, section_C, section_D

    def formuls(self, section_A, section_B, section_C, section_D):
        reverse_A = self.reverse_two(section_A)
        Y = array(section_C).dot(array(reverse_A))
        Delta = array(section_D) - Y.dot(array(section_B))
        X = matrix(reverse_A).dot(matrix(section_B))
        delta_reverse = self.reverse_two(Delta)

        Block_one = array(reverse_A) + (X.dot(array(delta_reverse))).dot(Y)
        Block_two = (- X.dot(array(delta_reverse)))
        Block_three = (- array(delta_reverse).dot(Y))
        Block_four = delta_reverse
        return Block_one, Block_two, Block_three, Block_four

    def combine(self, Block_one, Block_two, Block_three, Block_four):
        ROW1 = row_stack((Block_one, Block_three))
        ROW2 = row_stack((Block_two, Block_four))
        Matrix = column_stack((ROW1, ROW2))
        self.reverse = Matrix

    def eight_matrix(self):
        A, B, C, D = self.partiting(self.matrix)
        self.combine(*self.formuls(*self.partiting(A)))
        reverse_A = self.reverse
        Y = array(C).dot(array(reverse_A))
        Delta = array(D) - Y.dot(array(B))
        X = matrix(reverse_A).dot(matrix(B))
        self.combine(*self.formuls(*self.partiting(Delta)))
        delta_reverse = self.reverse

        block_one = array(reverse_A) + (X.dot(array(delta_reverse))).dot(Y)
        block_two = (- X.dot(array(delta_reverse)))
        block_three = (- array(delta_reverse).dot(Y))
        block_four = delta_reverse
        self.combine(block_one, block_two, block_three, block_four)

    def check_size(self):
        if self.matr_len == 8:
            try:
                return self.eight_matrix()
            except Exception:
                return False
        elif self.matr_len == 4:
            try:
                self.combine(*self.formuls(*self.partiting(self.matrix)))
                return self.reverse
            except Exception:
                return False
        else:
            return False
