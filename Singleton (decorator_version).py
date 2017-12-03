def singleton(klass):

    instances = None

    def wrap(*args, *kwargs):
        nonlocal instances

        if instances == None:
            instances = klass(*args, *kwargs)

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


z = Person('Bob', 87, 26)
x = Person('Jack', 0, 0)

print(z, x)

print(z.hours, x.hours)
