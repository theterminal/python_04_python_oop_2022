from project.client import Client


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []                                      # objects - list with all the meals
        self.clients_list = []                              # objects - list with all the clients

    def __check_if_client_exists(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return True

    def __check_if_meal_is_in_menu(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return True

    def __check_if_menu_not_ready(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

    def __find_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def __find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def __check_for_order(self, client):
        if len(client.shopping_cart) == 0:
            raise Exception('There are no ordered meals!')

    def register_client(self, client_phone_number: str):
        if self.__check_if_client_exists(client_phone_number):
            raise Exception('The client has already been registered!')
        self.clients_list.append(Client(client_phone_number))
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in ['Starter', 'MainDish', 'Dessert']:
                self.menu.append(meal)

    def show_menu(self):
        self.__check_if_menu_not_ready()

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_if_menu_not_ready()
        if not self.__check_if_client_exists(client_phone_number):
            self.register_client(client_phone_number)

        current_client = self.__find_client(client_phone_number)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if not self.__check_if_meal_is_in_menu(meal_name):
                raise Exception(f'{meal_name} is not on the menu!')
            current_meal = self.__find_meal(meal_name)

            if current_meal.quantity < meal_quantity:
                raise Exception(f'Not enough quantity of {type(current_meal).__name__}: {current_meal.name}!')

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            current_meal = self.__find_meal(meal_name)
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * meal_quantity
            current_meal.quantity -= meal_quantity
            current_client.ordered_quantities[current_meal.name] = meal_quantity        # used to reset the shopping cart if order is cancelled

        ordered_meal_names = []
        for ordered_meal in current_client.shopping_cart:
            ordered_meal_names.append(ordered_meal.name)

        return f"Client {current_client.phone_number} successfully ordered {', '.join(ordered_meal_names)} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        self.__check_for_order(client)
        for meal_name, meal_quantity in client.ordered_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += meal_quantity
        client.shopping_cart = []
        client.ordered_quantities = {}
        client.bill = 0.0

        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        self.__check_for_order(client)
        bill_to_be_paid = client.bill
        client.shopping_cart = []
        client.ordered_quantities = {}
        client.bill = 0.0
        self.RECEIPT_ID += 1
        return f'Receipt #{self.RECEIPT_ID} with total amount of {bill_to_be_paid:.2f} was successfully paid for {client_phone_number}.'

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'
