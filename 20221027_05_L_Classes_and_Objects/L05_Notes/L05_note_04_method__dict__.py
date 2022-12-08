# 20221027 - Python OOP - Classes and Objects
# Note 03 - Method __dict__


class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


a = MyClass(2)
b = MyClass(3)

print(MyClass.__dict__)         # {'__module__': '__main__', 'class_variable': 1, '__init__': <function MyClass.__init__ at 0x100da0ca0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
print(a.__dict__)               # { 'instance_variable': 2 }
print(b.__dict__)               # { 'instance_variable': 3 }

print(MyClass(122))             # <__main__.MyClass object at 0x109daf1c0>
print(MyClass(123).__dict__)    # {'instance_variable': 123}
