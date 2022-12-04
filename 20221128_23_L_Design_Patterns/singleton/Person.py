def singleton(cls):
    instance = [None]

    def wrapper(*args):
        if instance[0] is None:
            instance[0] = cls(*args)
        return instance
    return wrapper


@singleton
class Person:
    pass
