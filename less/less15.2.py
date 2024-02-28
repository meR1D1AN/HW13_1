from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Develop(Employee):

    def work(self):
        print("Write some code")

    def code(self):
        pass


class Accountant(Employee):

    def work(self):
        print("Counting")


dev1 = Develop()
abc1 = Accountant()

print(dev1)
print(abc1)