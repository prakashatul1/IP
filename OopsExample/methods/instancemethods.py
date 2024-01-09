class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "secret 1"


    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


b1 = Book("Atushi","autgor1", 1223, 39)
b2 = Book("Atul", "autgor2", 233, 12)

print(b1)
print(b1.title)
print(b1.getprice())
print(b2.getprice())
b2.setdiscount(0.50)
print(b2.getprice())

print(b2._Book__secret)
# print(b2.__secret)


print(type(b2))
print(type(b1) == type(b1))

print(isinstance(b1, Book))

print(isinstance(b1, object))
