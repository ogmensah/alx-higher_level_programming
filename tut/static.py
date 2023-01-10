#!/usr/bin/python3

'''
How static method is created using decorators
'''
class Sum:

    @staticmethod
    def getSum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum

def main():
    print("Sum:", Sum.getSum(1,2,3,4,3))

main()

'''
creating static variable, num_of_dogs
'''
class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot = Dog("Spot")
    doug = Dog("Doug")
    spot.getNumOfDogs()
    doug.getNumOfDogs()

main()

'''
creating user defined or custom exception
'''
class DogNameError(Exception):
    def __init__(self, *args, **kargs):
        Excetption.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dog's name: ")

    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")


try:
    f = open("mydata2.txt")
except FileNotFoudError as ex:
    print("File was not found")
    print(ex.args)
else:
    print("File:", f.read())
    f.close()
finally:
    print("Finished working with file")

