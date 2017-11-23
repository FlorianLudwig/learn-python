print('10/hello.py')


class Animal:
    def __init__(self, name):
        self.name = name

    def announce(self):
        return 'My name is {}.'.format(self.name)


def Dog(Animal):
    def announce(self):
        return 'Woof'


def main():
    emmi = Dog('Emmi')
    print(emmi.announce())
    print(Animal.announce(emmi))


if __name__ == '__main__':
    main()
