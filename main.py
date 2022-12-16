from Prototype import Prototype
from Cake import Cake


def main():
    prototype = Prototype()
    prototype.register('cake', Cake())

    cake_1 = prototype.clone('cake', {'name': 'Медовик', 'comment': 'С шоколадной пропиткой'})
    cake_2 = prototype.clone('cake', {'name': 'Наполеон', 'comment': 'Стандартный наполеон'})

    Cake.print_cake(cake_1.name, cake_1.comment)
    Cake.print_cake(cake_2.name, cake_2.comment)


if __name__ == '__main__':
    main()
