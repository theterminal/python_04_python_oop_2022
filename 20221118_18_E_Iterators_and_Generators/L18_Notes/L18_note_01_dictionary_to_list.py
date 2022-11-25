# 20221118 - Python - Python OOP - Iterators and Generators
# Note 01 - dictionary to list conversion

dictionary = {'position': 15, 'name': 'Jimmy'}

list_from_dictionary = list(dictionary)
list_from_dictionary_keys = list(dictionary.keys())
list_from_dictionary_values = list(dictionary.values())
list_from_dictionary_items = list(dictionary.items())

print(list_from_dictionary)
print(list_from_dictionary_keys)
print(list_from_dictionary_values)
print(list_from_dictionary_items)
