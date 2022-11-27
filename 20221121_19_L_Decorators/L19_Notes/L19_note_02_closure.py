# 20221121 - Python - Python OOP - Decorators
# Note 02 - Closure


"""
Python allows a nested function to access the outer scope of the enclosing function.
This is called closure and is a critical concept in decorators.

"""


def print_message(message):
    def message_sender():
        print(message)

    message_sender()


print_message('Some random message')
