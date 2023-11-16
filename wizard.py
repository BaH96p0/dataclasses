class Wizard:
    def __init__(self, name, rating, age_appearance):
        self.name = name
        self.rating = rating
        self.age_appearance = age_appearance

    def change_rating(self, value):
        self.rating = max(1, min(100, self.rating + value))

        if value > 0:
            self.age_appearance = max(18, self.age_appearance - abs(value) // 10)

        elif value < 0:
            self.age_appearance += abs(value) // 10

    def __add__(self, other):
        if isinstance(other, str):
            length = len(other)
            self.rating += length
            self.age_appearance = max(18, self.age_appearance - length // 10)
            return self
        else:
            return NotImplemented

    def __call__(self, number):
        return (number - self.age_appearance) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.age_appearance} years old"

    def __lt__(self, other):
        return (self.rating, self.age_appearance, self.name) < (other.rating, other.age_appearance, other.name)

    def __le__(self, other):
        return (self.rating, self.age_appearance, self.name) <= (other.rating, other.age_appearance, other.name)

    def __eq__(self, other):
        return (self.rating, self.age_appearance, self.name) == (other.rating, other.age_appearance, other.name)

    def __ne__(self, other):
        return (self.rating, self.age_appearance, self.name) != (other.rating, other.age_appearance, other.name)

    def __gt__(self, other):
        return (self.rating, self.age_appearance, self.name) > (other.rating, other.age_appearance, other.name)

    def __ge__(self, other):
        return (self.rating, self.age_appearance, self.name) >= (other.rating, other.age_appearance, other.name)


wizard1 = Wizard("Gandalf", 90, 60)
wizard2 = Wizard("Dumbledore", 95, 50)

print(wizard1)
print(wizard2)

wizard1.change_rating(5)
print(wizard1)

wizard1 += "Powerful spell"
print(wizard1)

result = wizard1(30)
print(f"Result of the calculation: {result}")

if wizard1 > wizard2:
    print(f"{wizard1.name} is more powerful than {wizard2.name}")
else:
    print(f"{wizard2.name} is more powerful than {wizard1.name}")
