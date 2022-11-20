from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value in ['Kiril', 'Alex', 'Mitch']:
            raise ValueError('The name you are trying to pass as woman is a male name!')
        self.__name = value

    @staticmethod
    def smart():
        return f'Very Intelligent!'

    def __str__(self):
        ...


class Child1(Parent):
    def __init__(self, name: str, age: int, condition: str):
        super().__init__(name, age)
        self.condition = condition

    def __str__(self):
        ...


class Child11(Child1):
    def __init__(self, name: str, age: int, condition: str):
        super().__init__(name, age, condition)

    def __str__(self):
        return f'{self.name} is {self.age}. She is {self.condition} and {self.smart()}'


class Child12(Child1):
    def __init__(self, name: str, age: int, condition: str):
        super().__init__(name, age, condition)

    def __str__(self):
        return f'{self.name} is {self.age}. She is {self.condition} and...'


a1 = Child12('Kristi', 25, 'Good')
a2 = Child11('Marty', 35, 'Great')

list_child = [a1, a2]
for child in list_child:
    print('\n__________________\n')
    print(child)
print('\n__________________\n')
