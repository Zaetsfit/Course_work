from numpy import *


class Inversed(object):
    def __init__(self, matr):
        self.matr = matr

    def check_determinant(self):
        return False if linalg.det(self.matr) == float(0) else True
