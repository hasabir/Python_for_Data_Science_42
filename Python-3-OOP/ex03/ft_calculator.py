class calculator:

    def __init__(self, vec) -> None:
        '''Constructor for calculator'''
        self.vec = vec

    def __add__(self, object):
        '''Add two vectors'''
        for i in range(len(self.vec)):
            self.vec[i] += object
        print(self.vec)

    def __mul__(self, object) -> None:
        for i in range(len(self.vec)):
            self.vec[i] *= object
        print(self.vec)

    def __sub__(self, object) -> None:
        for i in range(len(self.vec)):
            self.vec[i] -= object
        print(self.vec)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ValueError("Math error")
        for i in range(len(self.vec)):
            self.vec[i] /= object
        print(self.vec)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    10


if __name__ == "__main__":
    main()
