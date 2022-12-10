# Get all available methods for a specified class
# It prints out all available methods on a specific object


class TestClass:
    def __init__(self):
        pass


all_methods_of_object = dir(TestClass)
print('\n'.join([x for x in all_methods_of_object]))
