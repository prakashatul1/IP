class PapaClass:
    def __init__(self, name, title):
        self.name = name
        self.title = title

class Book(PapaClass):
    def __init__(self, name, title, price):
        super().__init__(name, title)
        self.price = price

class Publication(Book):
    def __init__(self, name, title, price, period):
        super().__init__(name, title, price)
        self.period = period

class Magazine(Publication):
    def __init__(self, name, title, price, period):
        super().__init__(name, title, price, period)

p1 = PapaClass('name1', "title1")
b1 = Book("name", "title", 12)
m1 = Magazine("digit","tech", 33, "monthly")

print(isinstance(p1, PapaClass))
print(isinstance(b1, PapaClass))
print(m1.title)

