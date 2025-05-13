class X:
    def __init__(self):
        print("X init")
        super().__init__()

class Y:
    def __init__(self):
        print("Y init")
        super().__init__()

class Z(X, Y):
    def __init__(self):
        print("Z init")
        super().__init__()

obj = Z()
print(Z.mro())