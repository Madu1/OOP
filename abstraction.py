# what is abstract class??

from abc import ABC, abstractmethod


# abstract class
class Computer(ABC):
    # abstract method
    @abstractmethod
    def process(self):
        # print("Running") --> nothing inside in the method body
        pass

    # concreate method
    def calculate(self):
        print("Calculate process time..")


class Laptop(Computer):
    def process(self):
        print("it's running..")


class Whiteboard(Computer):
    def write(self):
        print("write codes..")

    def process(self):
        print("practise algorithms")


class Desktop(Computer):
    def run(self):
        print("working with codes..")

    def process(self):
        print("Working with DS&A..")


class Programmer:
    def work(self, com):
        print("Solving bugs..")
        com.process()


# com = Computer()
com1 = Laptop()
white = Whiteboard()
desk = Desktop()

prog = Programmer()
prog2 = Programmer()
prog3 = Programmer()

prog.work(white)
prog2.work(com1)
prog3.work(desk)
com1.calculate()
# com1.process()
