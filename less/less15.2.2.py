class Employee:

    def __init__(self):
        self.pay = 50000
        super().__init__()


class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID += 1
        self.order_log()
        super().__init__()

    def order_log(self):
        print(f'{self.id}-й сотрудник')


class Develop(Employee, MixinLog):

    def __init__(self):
        super().__init__()

    def work(self):
        print('Write some code')

    def code(self):
        pass


dev1 = Develop()
dev2 = Develop()

print(dev2.pay)

print(Develop.__mro__)
