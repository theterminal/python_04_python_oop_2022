# 20221122 - Python - Python OOP - Decorators
# 03 - Bold, Italic, Underline - judge url: https://judge.softuni.org/Contests/Compete/Index/1947#2


def make_bold(func):
    def wrapper(*args):
        return f'<b>{func(*args)}</b>'
    return wrapper


def make_italic(func):
    def wrapper(*args):
        return f'<i>{func(*args)}</i>'
    return wrapper


def make_underline(func):
    def wrapper(*args):
        return f'<u>{func(*args)}</u>'
    return wrapper


# __________ Test Code 1 ____________

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


# __________ Test Code 2 ____________


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
