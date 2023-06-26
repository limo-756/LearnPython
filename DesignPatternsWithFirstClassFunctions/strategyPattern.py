from abc import ABC, abstractmethod
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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """Return a positive discount based on strategy"""


class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity > 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        # discount = sum(item.total * 0.1 for item in order.items if item.quantity >= 20)

        for item in order.items:
            if item.quantity >= 20:
                discount += item.total() * 0.1

        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        items = set(item.product for item in order.items)
        return order.total() * 0.07 if len(items) >= 10 else 0


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0),
    ]

    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))

    banana_cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5)
    ]
    print(Order(joe, banana_cart, BulkItemPromo()))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, LargeOrderPromo()))
    print(Order(joe, cart, LargeOrderPromo()))