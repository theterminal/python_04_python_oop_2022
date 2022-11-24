# 20221117 - Python - Python OOP - Iterators and Generators
# 06 - Reverse String - judge url: https://judge.softuni.org/Contests/Practice/Index/1944#5


def reverse_text(text: str):
    i_current = -1
    i_end = -len(text)
    while i_current >= i_end:
        yield text[i_current]
        i_current -= 1


for char in reverse_text("step"):
    print(char, end='')
