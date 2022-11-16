from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []                 # Customer objects
        self.dvds = []                       # DVD objects

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        # if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:                # use line 1, 2 or 3 - it's the same
        # if len(self.customers) < MovieWorld.customer_capacity():              # use line 1, 2 or 3 - it's the same
        if len(self.customers) < self.customer_capacity():                      # use line 1, 2 or 3 - it's the same
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in self.dvds if x.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return f'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = [x for x in self.customers if x.id == customer_id][0]
        dvd = [x for x in self.dvds if x.id == dvd_id][0]

        if dvd not in customer.rented_dvds:
            return f'{customer.name} does not have that DVD'
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        return "\n".join([
            *[str(x) for x in self.customers],
            *[str(x) for x in self.dvds]
        ])
