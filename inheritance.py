class Dog:
    __name = None

    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'Just a normal dog named {self.name}'


class BraveDog(Dog):
    __medal = None

    @property
    def medal(self):
        return self.__medal

    @medal.setter
    def medal(self, medal):
        self.__medal = medal

    def __str__(self):
        if self.__medal:
            return f'{self.name} with {self.__medal} medal'
        return f'{self.name} is a brave dog but no medal'

if __name__ == "__main__":
    dog = Dog("jojo")
    print(dog)

    brave_dog = BraveDog()
    brave_dog.name = "fufu"
    brave_dog.medal = "Gold"
    print(brave_dog)

