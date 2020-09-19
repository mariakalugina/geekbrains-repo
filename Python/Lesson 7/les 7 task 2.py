class Clothes:
    def __init__(self,title):
        self.title = title


class Suit(Clothes):
    def __init__(self, height):
        self.title = "Костюм"
        self.h = height

    @property
    def get_cloth(self):
        return 2 * self.h + 0.3


class Coat(Clothes):
    def __init__(self, size):
        self.title = "Пальто"
        self.size = size

    @property
    def get_cloth(self):
        return round(self.size/ 6.5 + 0.5,2)


newSuit=Suit(1.93)
newCoat= Coat(3)

print(f"Количество ткани для изделия {newSuit.title} = {newSuit.get_cloth}")
print(f"Количество ткани для изделия {newCoat.title} = {newCoat.get_cloth}")