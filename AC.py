from dataclasses import dataclass, field


class AirCastle:
    def __init__(self, height, cloud_count, color):
        self.height = height
        self.cloud_count = cloud_count
        self.color = color

    def change_height(self, value):
        self.height = max(0, self.height + value)

    def __add__(self, n):
        self.cloud_count += n
        self.height += n // 5

    def __call__(self, transparency):
        return self.height // transparency * self.cloud_count

    def __str__(self):
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.cloud_count} clouds"

    def __lt__(self, other):
        if self.cloud_count != other.cloud_count:
            return self.cloud_count < other.cloud_count
        elif self.height != other.height:
            return self.height < other.height
        else:
            return self.color < other.color

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.cloud_count == other.cloud_count and self.height == other.height and self.color == other.color

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


castle1 = AirCastle(100, 20, "Blue")
castle2 = AirCastle(80, 25, "Red")

print(castle1)
print(castle2)

castle1.change_height(-50)
castle2 + 10

print(castle1(2))
print(castle2(3))

if castle1 < castle2:
    print("Castle 1 has fewer clouds than Castle 2")
elif castle1 == castle2:
    print("Castle 1 and Castle 2 are equal")
else:
    print("Castle 2 has fewer clouds than Castle 1")
