class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #This special methods string function returns whatever is inside of the
    # def __str__(self): method.
    #This allows the user to store the class in a variable and use the print() function on that variable to return string interpolation.
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    #This special length function returns whatever is inside the def __len__(self): method.  
    #This allows user to store the number of pages that is passed to the function and then when the program requires the length of the class. It will return self.pages
    def __len__(self):
        return self.pages

    #This method will print out the message below if the del method is invoked.
    def __del__(self):
        print("A book object has been deleted")

#place information in the designated slots for parameters.
b = Book("Book title", "me", 123)

#print an output for the data in the class
print(b)
# print(str(b))



#return the length of b.
print(len(b))

