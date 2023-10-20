import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.create_random_matrix()

    def create_random_matrix(self):
        self.matrix = []
        for i in range(self.rows):
            row = [random.randint(-10, 10) for _ in range(self.cols)]
            self.matrix.append(row)
        return self.matrix

    def print_matrix(self):
        result = ""
        for row in self.matrix:
            result += "\n"
            for num in row:
                result += str(num) + " "
        return result[1:]

    def __repr__(self):
        return self.print_matrix()

    def __add__(self, other):


my_matrix = Matrix(4, 5)
print(my_matrix)
# rows = 5
# cols = 4
#
# my_matrix(rows,cols)
