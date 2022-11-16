class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()          # option 3
        Customer.id += 1                          # option 3

        # self.id = Customer.id                   # option 1
        # Customer.id += 1                        # option 1

        # self.id = __class__.id                  # option 2
        # __class__.id += 1                       # option 2

    # option 3: the following classmethod
    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
