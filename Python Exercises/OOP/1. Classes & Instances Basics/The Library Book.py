class Book:
    def __init__(self, book_title, book_author):
        self.book = book_title
        self.author = book_author
        self.is_available = True
    def borrow_book(self):
        if self.is_available == True:
            self.is_available = False
            return f"You Have Borrowed {self.book} by {self.author} successfully"
        else:
            return f"Sorry, {self.book} is currently not available"
    def return_book(self):
        self.is_available = True
        return f"Thank you for returning {self.book}"

books = Book("Atomic Habits", "James Clear")
print(books.borrow_book())
print(books.borrow_book())
print(books.return_book())