# 20221110 - Python - Python OOP - Polymorphism and Abstraction
# 03 - Playing - judge url: https://judge.softuni.org/Contests/Practice/Index/1942#1


def start_playing(obj):
    return obj.play()


print('\n____________ Test Code 1 ____________\n')


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))


print('\n____________ Test Code 1 ____________\n')


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))
