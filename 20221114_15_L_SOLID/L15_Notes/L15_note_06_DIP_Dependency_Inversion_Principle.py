# 20221114 - Python - Python OOP - SOLID
# Note 06 - DIP (Dependency Inversion Principle)


"""
Interesting design principle by which we protect our code by making it independent of things that are
fragile, volatile, or out of our control.

Depend on abstractions, not on concretions.
High-level modules should not depend on low-level modules.
Both should depend on abstractions.
Abstractions should not depend on details.
Details should depend on abstractions.

Software engineering technique for defining the dependencies among objects.

Why use Dependency Injection?
    *) Decreases coupling between a class and its dependency.
    *) Can be applied to legacy code as a refactoring because it doesn’t require any change in code behaviour.
    *) Allows a client to remove all knowledge of a concrete implementation that it needs to use.

"""


class Email:
    def send_email(self):
        pass


class Notification:
    def __init__(self):
        self._email = Email()

    def promotional_notification(self):
        self._email.send_email()


# Example: Constructor Injection


class MessageService:
    def send_message(self):
        pass


class Email(MessageService):
    def send_message(self):
        pass


class Notification:
    def __init__(self, service: MessageService):
        self._service = service

    def promotional_notification(self):
        self._service.send_message()
