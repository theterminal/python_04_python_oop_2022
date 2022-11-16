# 20221107 - Python - Python OOP
# Note 04 - Class Methods & Static Methods - Example 01


class Validator:
    @staticmethod
    def raise_if_str_is_null_or_empty(value, error_message='Invalid string value provided'):
        if not value.strip():
            raise ValueError(error_message)

    @staticmethod
    def raise_if_num_not_in_range(value, min_range, max_range, error_message='Age must be withing specified range'):
        if value < min_range or value > max_range:
            raise ValueError(error_message)


class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_str_is_null_or_empty(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_num_not_in_range(value, self.MIN_AGE, self.MAX_AGE)
        self.__age = value

    def __str__(self):
        return f'Person is {self.__name} and age is {self.__age}'


class Employee(Person):
    MIN_AGE = 21
    MAX_AGE = 40

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f'Employee is {self.name}, age is {self.age} and salary is {self.salary}'


# Test Code 1 (Person's age must be in rage [0: 150], Employee's age must be in range [21: 40])
# -------------
p_1 = Person('Peter', 25)                                 # If age is not within (0: 150] it'll trow an error, if name is not a str also
e_1 = Employee('George', 22, 1_555)
print(str(p_1) + '\n' + str(e_1))
print()
