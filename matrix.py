class Matrix:

    def __init__(self, height, width):
        self.matrix = []
        self.height = height
        self.width = width

        for i in range(height):
            self.matrix.append([])
            for j in range(width):
                self.matrix[i].append(int(input("Enter a value for position {}, {}".format(str(i + 1), str(j + 1)))))

    def __str__(self):
        return str(self.matrix)

    def __len__(self):
        return int(self.height)

    def __add__(self, other):
        if self.height == len(other) and self.width == len(other.matrix[0]):
            summed_matrix = []
            for i in range(self.height):
                summed_matrix.append([])
                for j in range(self.width):
                    summed_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])

            return summed_matrix

        raise Exception('Invalid matrix addition; both matrices must have the same number of columns and rows')

    def row_swap(self, row_one, row_two):
        temp_row = self.matrix[row_one - 1]
        self.matrix[row_one - 1] = (self.matrix[row_two - 1])
        self.matrix[row_two - 1] = temp_row

    # def row_replace(self, source_row, target_row, scalar):

