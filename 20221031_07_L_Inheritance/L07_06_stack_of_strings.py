# 20221031 - Python OOP - Inheritance
# 06 - Stack Of Strings


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(str(element))
        # return self.data

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'
