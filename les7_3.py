import time


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __del__(self):
        print('Я твой отец')

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return type(self)(other.name, self.surname)


class GarageIter:
    def __init__(self, box):
        self.__idx = 0
        self.__box = box

    def __next__(self):
        while self.__idx < len(self.__box):
            self.__idx += 1
            if self.__box[self.__idx - 1].vin:
                return self.__box[self.__idx - 1]

        raise StopIteration


class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def set_car(self, car):
        self.__box.append(car)

    def __getitem__(self, item):
        return self.__box[item]

    def __iter__(self):
        return GarageIter(self.__box)


class Car:
    __slots__ = ('name', 'vin')

    def __init__(self, name, vin=None):
        self.name = name
        self.vin = vin

    def __str__(self):
        return self.name


if __name__ == '__main__':
    garage = Garage('Crazy Monkey')
    garage.set_car(Car('Ford', 14444))
    garage.set_car(Car('GMC', 464547547))
    garage.set_car(Car('Pontiac'))

    for car in garage:
        print(car)
    # hum = Human('Dart', "Vaider")
    # hum2 = Human('Princess', 'Lea')

    # hum3 = hum + hum2
    # hum3 = hum.__add__(hum2)

    # print(hum3)
