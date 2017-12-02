class Person:  

    IS = None

    def __init__(self, name, hours, rate): 
        self.name = name
        self.hours = hours
        self.rate = rate

    def __new__(cls, *args, **kwargs):

        if cls.IS == None:

            cls.IS = object.__new__(Person)
            return cls.IS

        return cls.IS



    def pay(self):
        return self.hours * self.rate


z = Person('Bob', 14, 4)
x = Person('Jack', 44, 4)

print(z, x)

print(z.hours, x.hours)
