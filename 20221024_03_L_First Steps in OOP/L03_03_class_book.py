# 20221024 - Python OOP - First Steps in OOP
# 03 - Class Book - judge url: https://judge.softuni.org/Contests/Practice/Index/1934#2


# --------------------- version 1 --------------------- judge 100%


class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
