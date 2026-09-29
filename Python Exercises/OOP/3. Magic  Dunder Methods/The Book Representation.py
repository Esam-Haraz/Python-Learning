class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

book_title = "Python Crash Course"
book_author = "Eric Matthes"
book_pages = 544
customer_book = Book(book_title, book_author, book_pages)
print(customer_book)
