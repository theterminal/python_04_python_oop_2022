from project.worker import Worker


class Keeper(Worker):
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age, salary)
