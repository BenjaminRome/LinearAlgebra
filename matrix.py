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

    def __add__(self, other):
        

    def row_swap(self, row_one, row_two):
        temp_row = []
        temp_row = self.matrix[row_one - 1]
        self.matrix[row_one - 1] = (self.matrix[row_two - 1])
        self.matrix[row_two - 1] = temp_row

    def row_replace(self, source_row, target_row, scalar):

