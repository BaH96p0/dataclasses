class GoodIfrit:
    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = goodness

    def change_goodness(self, value):
        self.goodness = max(0, self.goodness + value)

    def __add__(self, number):
        new_height = self.height + number
        return GoodIfrit(new_height, self.name, self.goodness)

    def __call__(self, argument):
        return argument * self.goodness // self.height

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"

    def __lt__(self, other):
        if self.goodness != other.goodness:
            return self.goodness < other.goodness
        elif self.height != other.height:
            return self.height < other.height
        else:
            return self.name < other.name

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.goodness == other.goodness and self.height == other.height and self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


# Пример использования
gi = GoodIfrit(80, "Hazrul", 3)
gi.change_goodness(4)
print(gi)

gi1 = gi + 15
print(gi1)

result = gi(31)
print(result)

gi = GoodIfrit(80, "Hazrul", 3)
gi1 = GoodIfrit(80, "Dalziel", 1)
print(gi < gi1)

gi1.change_goodness(2)
print(gi > gi1)

print(gi)
print(gi1)
