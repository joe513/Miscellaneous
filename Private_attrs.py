
def Private(*items):

    def decor(klass):

        privates = items

        class Acces:

            def __init__(self, *args, **kwargs):
                self.obj = klass(*args, **kwargs)

            def __getattr__(self, item):
                if item in privates:
                    raise TypeError('This item is private')

                return getattr(self.obj, item)

            def __setattr__(self, key, value):
                if key in privates:
                    raise TypeError('This item is private')

                if key == 'obj':
                    self.__dict__[key] = value

                object.__setattr__(self.obj, key, value)

        return Acces
    return decor


@Private()
class Person:

    def __init__(self):
        self.name = 'Bob'
        self.age = 50


b = Person()
print(b.name)
print(b.age)
