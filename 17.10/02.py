class MatrixIterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = 0
        self.col = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.row < len(self.matrix):
            if self.col < len(self.matrix[self.row]):
                result = self.matrix[self.row][self.col]
                self.col += 1
                return result
            else:
                self.row += 1
                self.col = 0
                return next(self)
        else:
            raise StopIteration


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix_iterator = MatrixIterator(matrix)

for element in matrix_iterator:
    print(element)
