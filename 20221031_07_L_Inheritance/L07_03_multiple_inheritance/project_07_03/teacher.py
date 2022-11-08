from project_07_03.person import Person
from project_07_03.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
