# method overriding
class A:
    def show(self):
        print("in A Show")


class B:
    def show(self):
        print("in B Show")


a = B()
a.show()
