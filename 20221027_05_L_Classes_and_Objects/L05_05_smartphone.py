# 20221027 - Python OOP - Classes and Objects
# 05 - Smartphone - judge: https://judge.softuni.org/Contests/Practice/Index/1936#4


# --------------------- version 1 ------------------------ judge: 100%


class Smartphone:
    def __init__(self, memory: float):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if app_memory <= self.memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f'Installing {app}'
        elif not self.is_on:
            return f'Turn on your phone to install {app}'
        else:
            return f'Not enough memory to install {app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
