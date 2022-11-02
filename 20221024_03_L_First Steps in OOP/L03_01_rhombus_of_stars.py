# 20221024 - Python OOP - First Steps in OOP
# 01 - Rhombus of Stars - judge: https://judge.softuni.org/Contests/Practice/Index/1934#0


# --------------------- version 3 ------------------------ judge: 100%


def print_row(figure_size, row_size, symbol):
    print(' ' * (figure_size - row_size), end='')
    for _ in range(1, row_size + 1):
        print(f'{symbol} ', end='')
    print()


def draw_figure(n, symbol):
    for row in range(1, n + 1):
        print_row(n, row, symbol)

    for row in range(n - 1, -1, -1):
        print_row(n, row, symbol)


n = int(input())
draw_figure(n, '*')


# --------------------- version 2 ------------------------ judge: 100%


def print_row(figure_size, row_size):
    print(' ' * (figure_size - row_size), end='')
    for _ in range(1, row_size + 1):
        print('* ', end='')
    print()


n = int(input())

for row in range(1, n + 1):
    print_row(n, row)


for row in range(n - 1, -1, -1):
    print_row(n, row)


# --------------------- version 1 ------------------------ judge: 100%


n = int(input())

for row in range(1, n + 1):
    print(' ' * (n - row), end='')
    for col in range(1, row + 1):
        print('* ', end='')
    print()

for row in range(n - 1, -1, -1):
    print(' ' * (n - row), end='')
    for col in range(1, row + 1):
        print('* ', end='')
    print()
