from Animal import Animal


class Cat(Animal):
    def __init__(self, nickname, age, weight, is_hungry):
        super().__init__(nickname)
        self._age = age
        self._weight = weight
        self._is_hungry = is_hungry

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @property
    def is_hungry(self):
        return self._is_hungry

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @is_hungry.setter
    def is_hungry(self, new_is_hungry):
        self._is_hungry = new_is_hungry

    def __str__(self) -> str:
        return f"{self.nickname} {self._age} {self._weight} {self._is_hungry}"