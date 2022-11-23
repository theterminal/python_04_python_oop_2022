# 20221117 - Python - Python OOP - Iterators and Generators
# 03 - Vowels - judge url: https://judge.softuni.org/Contests/Practice/Index/1944#2


class vowels:
    ALL_VOWELS = ['A', 'O', 'U', 'E', 'I', 'Y', 'a', 'o', 'u', 'e', 'i', 'y']

    def __init__(self, text: str):
        self.text = text
        self.vowels_in_text = [ch for ch in self.text if ch in vowels.ALL_VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration
        return self.vowels_in_text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
