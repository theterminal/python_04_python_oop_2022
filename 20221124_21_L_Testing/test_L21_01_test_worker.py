# 20221124 - Python - Python OOP - Testing
# 01 - Test Worker - judge url: https://judge.softuni.org/Contests/Practice/Index/1948#0


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Jonny', 1_000, 100)

    def test_correct_initializing(self):                                                     # test 1                   : 1, x, x, x, x, x      16%
        self.assertEqual('Jonny', self.worker.name)
        self.assertEqual(1_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_of_money_for_worker_when_working(self):                               # test 1, 2                : 1, x, x, 2, x, x      33%
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_decrease_energy_of_worker_when_working(self):                                   # test 1, 2, 3             : 1, x, x, 2, 3, x      50%
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_raise_exception_when_worker_tries_to_work_with_0_or_negative_energy(self):      # test 1, 2, 3, 4          : 1, x, 4, 2, 3, x      66%
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_energy_after_rest(self):                                               # test 1, 2, 3, 4, 5       : 1, 5, 4, 2, 3, x      83%
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_correct_info(self):                                                         # test 1, 2, 3, 4, 5, 6    : 1, 5, 4, 2, 3, 6      100%
        self.assertEqual('Jonny has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
