class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

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

