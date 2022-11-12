# 20221103 - Python - Python OOP - Encapsulation
# note 13 - Example of 'getattr()', 'setattr()', 'hasattr()', 'delattr()'


class Employee:
    name = 'Diyan'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)


employee = Employee()
print(getattr(employee, 'name'))            # Diyan
print(hasattr(employee, 'name'))            # True
setattr(employee, 'height', 152)
print(getattr(employee, 'height'))          # 152
delattr(Employee, 'salary')
