# 20221122 - Python - Python OOP - Decorators
# 06 - HTML tags - judge url: https://judge.softuni.org/Contests/Compete/Index/1947#5


# ------------------ version 1 --------------------


def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return wrapper
    return decorator


# ____ Test Code 1 ____


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings('Hello', ' you!'))


# ____ Test Code 2 ____


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))


# ------------------ version 2 ----- extended -----


def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return wrapper
    return decorator


# ____ Test Code 1 ____


@tags('html')
@tags('body')
@tags('div')
@tags('article')
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings('Hello', ' you!', 'From inside the paragraph...'))
