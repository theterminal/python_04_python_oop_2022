# 20221103 - Python - Python OOP - Encapsulation
# Note 04 - Getter and Setter Methods (in other languages mainly)


"""

Used to access and change the private variables as they are part of the class.
Mainly setters and getters are used when data validation is needed!

"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)

    def get_age(self):                  # getter
        print(self.__age)

    def set_age(self, age):             # setter
        self.__age = age


person = Person('Peter', 25)

# accessing data using class method
person.info()	                        # Peter
# 		                                  25

# changing age using setter
person.get_age()                        # 25
person.set_age(26)
person.get_age()	                    # 26
