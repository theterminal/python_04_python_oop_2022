# 20221117 - Python - Python OOP - Iterators and Generators
# Note 04 - Generator Expression


"""
Generators can be easily created using generator expressions.
Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.
The syntax for generator expression is similar to that of a list comprehension.
The difference between them is that generator expression produces one item at a time.
"""


print('\n________ example 1 __________\n')


# list comprehension solution for squaring each item from a list.
my_list = [1, 3, 6, 10]                                             # Initialize the list
print([x**2 for x in my_list])                                      # Output: [1, 9, 36, 100]


print('\n_________ same problem solved using generator expression ___________ \n')


# same thing can be done using generator expression
my_list = [1, 3, 6, 10]                                             # Initialize the list
print((x**2 for x in my_list))                                      # Output: <generator object <genexpr> at 0x0000000002EBDAF8>


print('\n_________ printing out the result __________\n')


my_list = [1, 3, 6, 10]                                             # Initialize the list
# a = ((x**2 for x in my_list))                                     # could use either syntax (assign generator to a var or not)
for num in ((x**2 for x in my_list)):
    print(num)
