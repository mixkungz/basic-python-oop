import abc

#Version 1
# class Dog:
#     def bark(self):
#         pass

# class BraveDog(Dog):
#     def walk(self):
#         print('I\'m walking dude.')

#########################################################################################################

#Version 2 (https://www.python.org/dev/peps/pep-3119/)
class Dog(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bark(self):
        pass

class BraveDog(Dog):
    def bark(self):
        print('Don\'t command me human.')
    def walk(self):
        print('I\'m walking dude.')

if __name__ == "__main__":
    brave_dog = BraveDog()
    brave_dog.walk()
