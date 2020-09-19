class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell > other.cell):
            return Cell(self.cell - other.cell)
        else:
            return Cell(other.cell - self.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        if (self.cell > other.cell):
            return Cell(self.cell // other.cell)
        else:
            return Cell(other.cell // self.cell)

    def make_order(self, number):
        return (("*"*number)+"\n")*(self.cell // number) + ("*" * (self.cell % number)) + "\n"

c1 = Cell(4)
c2 = Cell(16)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

print(c2.make_order(6))