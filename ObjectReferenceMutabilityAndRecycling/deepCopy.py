import copy


class Bus:

    def __init__(self, passengers) -> None:
        super().__init__()
        self.passengers = list(passengers)

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop(self, passenger):
        self.passengers.remove(passenger)


if __name__ == '__main__':
    bus1 = Bus(["alice", "john", "bintu", "tintu"])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)

    print("Bus1 Id : ", id(bus1))
    print("Bus2 Id : ", id(bus2))
    print("Bus3 Id : ", id(bus3))

    bus1.drop('alice')
    print("bus1 : ", bus1.passengers)
    print("bus2 : ", bus2.passengers)
    print("bus3 : ", bus3.passengers)

    print("id passengers of bus1 ", id(bus1.passengers))
    print("id passengers of bus2 ", id(bus2.passengers))
    print("id passengers of bus3 ", id(bus3.passengers))

    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)
    c = copy.deepcopy(a)
    print(c)
