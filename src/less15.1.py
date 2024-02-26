class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.pay + other.pay
        raise TypeError


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.1)


emp1 = Employee("Ivan", "Ivanov", 50000)
dev1 = Developer("Fedor", "Fedorov", 50000, "Python")

res1 = emp1 + dev1

print(res1)
