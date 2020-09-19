class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        newstr = ""
        for item in self.matrix:
            for i in item:
                newstr = newstr + f"{i}" + "  "
            newstr = newstr + "\n"
        return newstr

    def __add__(self, other):
        newMatrix = []
        resultMatrix = Matrix([])
        if len(self.matrix) == len(other.matrix):
            for n in range(len(self.matrix)):
                if len(self.matrix[n]) == len(other.matrix[n]):
                    newList = []
                    for i in range(len(self.matrix[n])):
                        newList.append(self.matrix[n][i] + other.matrix[n][i])
                    newMatrix.append(newList)
                else:
                    return ("Невозможно выполнить сложение. Матрицы должны быть одинакового размера")
            resultMatrix = Matrix(newMatrix)
            return resultMatrix
        else:
            return ("Невозможно выполнить сложение. Матрицы должны быть одинакового размера")



m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
m2 = Matrix([[2, 3, 4], [3, 4, 5], [4, 6, 7]])
m3 = Matrix([[2, 3], [3, 4], [4, 6]])

print(m1 + m2)
print(m1+m3)
