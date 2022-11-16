# 20221107 - Python - Python OOP
# 03 - Shop - judge url: https://judge.softuni.org/Contests/Practice/Index/2430#2


from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate (value):
            if (i + 1) == len(value) or roman_numbers[c] >= roman_numbers[value[i + 1]]:
                result += roman_numbers[c]
            else:
                result -= roman_numbers[c]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        error_message = 'wrong type'
        if not isinstance(value, str):
            return error_message

        try:
            number = int(value)
            return cls(number)
        except:
            return error_message


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
