class HuntedBus:

    def __init__(self, passengers=[]) -> None:
        super().__init__()
        self.passengers = passengers

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


if __name__ == '__main__':
    bus1 = HuntedBus(['Alice', 'Bill'])
    print(bus1.passengers)
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)

    bus2 = HuntedBus()
    bus2.pick('Mohan')
    print(bus2.passengers)

    bus3 = HuntedBus()
    print(bus3.passengers)

    bus3.pick('Ram')
    print(bus2.passengers)

    print(bus2.passengers is bus3.passengers)

