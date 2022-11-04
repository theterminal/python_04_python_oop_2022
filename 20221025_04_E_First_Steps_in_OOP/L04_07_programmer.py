# 20221025 - Python OOP - First Steps in OOP
# 07 - Programmer - judge: https://judge.softuni.org/Contests/Compete/Index/1935#6


# --------------------- version 1 ------------------------ judge: 100%


class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        else:
            return f'{self.name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and new_language != self.language:
            previous_language = self.language
            self.language = new_language
            return f'{self.name} switched from {previous_language} to {new_language}'
        elif self.skills >= skills_needed and new_language == self.language:
            return f'{self.name} already knows {new_language}'
        else:
            return f'{self.name} needs {skills_needed - self.skills} more skills'


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
