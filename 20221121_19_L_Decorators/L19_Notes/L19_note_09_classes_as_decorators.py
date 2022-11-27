# 20221121 - Python - Python OOP - Decorators
# Note 09 - Classes as Decorators


class FuncLogger:
    _logfile = 'L19_note_09_out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)


@FuncLogger
def say_hi(name):
    print(f"Hi, {name}")


@FuncLogger
def say_bye(name):
    print(f"Bye, {name}")


say_hi("Peter")
say_bye("Peter")
