class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book("Book title", "me", 123)
print(b)
#printing b will output the Book initializatino at an address on the computer but not actually give us the data stored in the class


str(b)
#passing b to the str function will give us the address except in string form

