from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return f'Not enough budget'

        if self.__animal_capacity == len(self.animals):
            return f'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str):
        # _________ block 1 ___________ use block 1 or block 2 ______________
        # try:
        #     worker = next(filter(lambda x: x.name == worker_name, self.workers))
        # except StopIteration:
        #     return f'There is no {worker_name} in the zoo'
        #
        # self.workers.remove(worker)
        # return f'{worker_name} fired successfully'

        # _________ block 2 ___________ use block 2 or block 1 ______________
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        # _________ block 3 ___________ use block 3 or block 4 ______________
        sum_salaries = sum(w.salary for w in self.workers)

        # _________ block 4 ___________ use block 4 or block 3 ______________
        # sum_salaries = 0
        # for worker in self.workers:
        #     sum_salaries += worker.salary

        if sum_salaries > self.__budget:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= sum_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        cost_animals = sum(a.money_for_care for a in self.animals)

        if cost_animals > self.__budget:
            return f'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= cost_animals
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount: float):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda x: x.__class__.__name__ == 'Lion', self.animals))
        tigers = list(filter(lambda x: x.__class__.__name__ == 'Tiger', self.animals))
        cheetahs = list(filter(lambda x: x.__class__.__name__ == 'Cheetah', self.animals))

        result = [
            f'You have {len(self.animals)} animals',
            f'----- {len(lions)} Lions:'
        ]                                                   # could add this: *lions as 3-d element, instead of line 78
        result.extend(lions)

        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)

        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)

        return '\n'.join(str(x) for x in result)

    def workers_status(self):
        info = {'Caretaker': [], 'Vet': [], 'Keeper': []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]

        # ______________block 5 ______________ use block 5 or block 6 or block 7 _______
        # result = [
        #     f"You have {len(self.workers)} workers",
        #     f"----- {len(info['Keeper'])} Keepers:",
        #     *info['Keeper'],
        #     f"----- {len(info['Caretaker'])} Caretakers:",
        #     *info['Caretaker'],
        #     f"----- {len(info['Vet'])} Vets:",
        #     *info['Vet'],
        # ]

        # ______________block 6 ______________ use block 6 or block 5 or block 7 _______
        result = [f"You have {len(self.workers)} workers"]
        result += [f"----- {len(info['Keeper'])} Keepers:"]
        result += [*info['Keeper']]
        result += [f"----- {len(info['Caretaker'])} Caretakers:"]
        result += [*info['Caretaker']]
        result += [f"----- {len(info['Vet'])} Vets:"]
        result += [*info['Vet']]

        # ______________block 7 ______________ use block 7 or block 5 or block 6 _______
        # result = [f"You have {len(self.workers)} workers"]
        # result.append(f"----- {len(info['Keeper'])} Keepers:")
        # result.extend([*info['Keeper']])
        # result.append(f"----- {len(info['Caretaker'])} Caretakers:")
        # result.extend([*info['Caretaker']])
        # result.append(f"----- {len(info['Vet'])} Vets:")
        # result.extend([*info['Vet']])

        return '\n'.join(result)
