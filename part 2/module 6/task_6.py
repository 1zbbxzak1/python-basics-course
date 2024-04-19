print('Задание 6. Пицца')

# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и сколько
# заказывал у них в определённый период. Вам нужно структурировать эту информацию и определить,
# сколько всего пицц купил каждый заказчик.
#
# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида
# «Покупатель — название пиццы — количество заказанных пицц».
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту.
# Учитывайте, что один человек может заказать одну и ту же пиццу несколько раз.
#
# Пример
# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5
#
# Иванов:
# Мексиканская: 2
# Мясная: 3
# Пепперони: 3
#
# Петров:
# Де-Люкс: 2
# Интересная: 5

from collections import defaultdict


def parse_order(order):
    parts = order.split()
    customer = parts[0]
    pizza_name = ' '.join(parts[1:-1])
    quantity = int(parts[-1])
    return customer, pizza_name, quantity


def print_orders(orders_dict):
    for customer, pizzas in sorted(orders_dict.items()):
        print(f"\n{customer}:")
        for pizza, quantity in sorted(pizzas.items()):
            print(f"{pizza}: {quantity}")


def main():
    num_orders = int(input("Введите количество заказов: "))

    orders_dict = defaultdict(lambda: defaultdict(int))

    for i in range(1, num_orders + 1):
        order_str = input(f"Заказ {i}: ")
        customer, pizza_name, quantity = parse_order(order_str)
        orders_dict[customer][pizza_name] += quantity

    print_orders(orders_dict)


main()

print()
