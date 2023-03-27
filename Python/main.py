from Cat import *
from Dog import *
from Vet_service import *

cat1 = Cat('Барсик', 5, 25, False)
dog1 = Dog('Шарик', 7, 20, True)

list_animal = Vet_service()
list_animal.add_animal(cat1)
list_animal.add_animal(dog1)
list_animal.print()
list_animal.del_animal(cat1)
print('______________________')
list_animal.print()
