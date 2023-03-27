from hw.model.VendingMachine import VendingMachine
from hw.model.products.BottleOfWater import BottleOfWater
from hw.model.products.HotDrinks import HotDrinks
from hw.view.ConsoleUserInterface import ConsoleUserInterface


class Controller:

    def start(self):
        console = ConsoleUserInterface()
        list_hot_drinks = [HotDrinks('Milk', 2, 0.3, 80),
                           HotDrinks('Tea', 1, 0.4, 70),
                           HotDrinks('Coffee', 3, 1.0, 65)]
        list_bottle_of_water = [BottleOfWater('Fanta', 3, 0.5),
                                BottleOfWater('Sprite', 3.5, 0.45),
                                BottleOfWater('Cola', 3.2, 0.43)]
        vending_machine1 = VendingMachine()
        vending_machine2 = VendingMachine()
        console.print_message('-----Список горячих напитков добавлен в торговый автомат-----')
        vending_machine1.list_products = list_hot_drinks
        console.print_list_product(vending_machine1.list_products)
        console.print_message('-----Список бутилированных напитков добавлен в торговый автомат-----')
        vending_machine2.list_products = list_bottle_of_water
        console.print_list_product(vending_machine2.list_products)
        console.print_message('-----В горячие напитки добавлено какао-----')
        vending_machine1.add_at_list(HotDrinks('Какао', 2.5, 0.5, 70))
        console.print_list_product(vending_machine1.list_products)
        console.print_message('-----В бутилированные напитки добавлена минералка-----')
        vending_machine2.add_at_list(BottleOfWater('Минералка', 1.5, 0.5))
        console.print_list_product(vending_machine2.list_products)
        console.print_message('-----Получение Tea из торгового автомата-----')
        console.print_message(vending_machine1.get_product('Tea'))
        console.print_message('-----Получение Mirinda из торгового автомата-----')
        console.print_message(vending_machine2.get_product('Mirinda'))
