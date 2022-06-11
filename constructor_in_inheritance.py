class A:
    def __init__(self):
        print("It's A working")

    def feature1(self):
        print("Feature 1-A is workign")


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("It's B init")
#
#     def feature2(self):
#         print("Feature 2 is working")


class B:
    def __init__(self):
        print("It's B init")

    def feature1(self):
        print("Feature 1-B is workign")

    def feature2(self):
        print("Feature 2 is working")


class C(A,B):
    def __init__(self):
        super(C, self).__init__()
        print("It's C init")


    def feat(self):
        super(C, self).feature2()

a = C()
# a.feature1()
a.feat()
