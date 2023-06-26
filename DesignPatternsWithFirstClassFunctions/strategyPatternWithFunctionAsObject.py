from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price) -> None:
        super().__init__()
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, items, promotion=None) -> None:
        super().__init__()
        self.customer = customer
        self.items = list(items)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.items)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity > 1000 else 0


def bulk_item_promo(order):
    return sum(item.total() * 0.1 for item in order.items if item.quantity >= 20)


def large_order_promo(order):
    items = set(item.product for item in order.items)
    return order.total() * 0.07 if len(items) >= 10 else 0


def best_promo(order):
    strategies = [fidelity_promo, bulk_item_promo, large_order_promo]
    return max(strategy(order) for strategy in strategies)


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0),
    ]

    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    banana_cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5)
    ]
    print(Order(joe, banana_cart, bulk_item_promo))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, large_order_promo))
    print(Order(joe, cart, large_order_promo))

    print(best_promo(Order(joe, long_order, None)))
