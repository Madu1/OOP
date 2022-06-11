# Duck Typing
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyIde:

    def execute(self):
        print("Auto Complete")
        print("Conventional checking")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


# ide = PyCharm()
ide = MyIde()
lap = Laptop()
lap.code(ide)
