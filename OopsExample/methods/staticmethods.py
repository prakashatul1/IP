class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    def setTitle(self, newtitle):
        self.title = newtitle



print("book types: ", Book.getbooktypes())

b1 = Book("title1", "HARDCOVER")
b2 = Book("title2", "PAPERBACK")

theBooks = Book.getbooklist()
print(theBooks)
theBooks.append(b1)
theBooks.append(b2)
print(theBooks)

