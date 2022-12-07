class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []                           # objects (all meals)
        self.bill: float = 0.0                                  # total bill
        self.ordered_quantities = {}                            # used for cancel order method in the app

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not (value[0] == '0' and len(value) == 10 and value.isdigit()):
            raise ValueError('Invalid phone number!')
        self.__phone_number = value
