# Get all available methods for a specified class


class TestClass:
    def __init__(self):
        pass


# Prints out all available methods on a specific object
all_methods_of_object = dir(TestClass)
print('\n'.join([x for x in all_methods_of_object]))
