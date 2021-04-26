#Private variable
class Dog:
    __name = None

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print('Setting name')
        self.__name = name


if __name__ == "__main__":
    dog = Dog("jojo")
    print(dog.name)

    dog.name = "fufu"
    print(dog.name)
