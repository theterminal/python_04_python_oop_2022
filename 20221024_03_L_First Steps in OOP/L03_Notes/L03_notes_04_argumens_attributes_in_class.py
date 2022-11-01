# 20221024 - Python OOP - First Steps in OOP
# Notes 03


class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        self.is_published = False
        # number of attributes does NOT have to match the number of arguments!!!


book_1 = Book('Indiana Jones', 'Steven Spielberg', 200)
book_2 = Book('Star Wars', 'George Lucas', 600)

print(book_1.name)
print(book_2.name)
