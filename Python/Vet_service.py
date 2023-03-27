from Cat import Cat
from Dog import Dog
from Animal import Animal
class Vet_service:
    def __init__(self):
        list = []
        self._list = list

    def add_animal(self, animal):
        self._list.append(animal)

    def del_animal(self, animal):
        self._list.remove(animal)

    def print(self):
        for el in self._list:
            print(str(el))

    # def print(self):
    #     for i in range(2):
    #         for el in list(self._list[i]):
    #             print(str(el))
