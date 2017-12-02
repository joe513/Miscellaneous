def singleton(klass):

    instances = None

    def wrap(*args):
        nonlocal instances

        if instances == None:
            instances = klass(*args)

        return instances

    return wrap


@singleton
class Person: 

    def __init__(self, name, hours, rate): 
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


z = Person('Bob', 14, 4)
x = Person('Jack', 44, 4)

print(z, x)

print(z.hours, x.hours)
