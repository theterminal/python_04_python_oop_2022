# 20221121 - Python - Python OOP - Decorators
# Note 01 - Function returning function


"""
A function can also generate another function.
"""


def function_hello(name):
    def function_say_hi():
        return f'I say hi to {name}'
    return function_say_hi


print(function_hello('Marian'))                     # This returns the referent function
print(function_hello('Marian')())                   # This returns the result from the referent function

greeting_function = function_hello('Marty')         # assigns the function to a variable to call it later
print(greeting_function())                          # calling the previously assigned function to a variable
print(greeting_function)                            # prints out the address where the referent function lives


"""
The decorators lay on the above described principle.
"""
