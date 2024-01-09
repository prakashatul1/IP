class Book:

    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchaoters(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        r = 0
        for each in self.chapters:
            r += each.pages
        return r

class Chapter:

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


class Author:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


a1 = Author("Urvashi", "Urvi")
c1 = Chapter("School", 100)
c2 = Chapter("Long Distance", 200)
b1 = Book("Love Story", 199, a1)
b1.addchaoters(c1)
print(b1.author.lname)
print(b1.getbookpagecount())
b1.addchaoters(c2)
print(b1.getbookpagecount())

