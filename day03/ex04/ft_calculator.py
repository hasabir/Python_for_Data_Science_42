class calculator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is: ", sum(x*y for x, y in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        lst: list[float] = []
        for i in range(len(V1)):
            lst.append(V1[i] + V2[i])
        formatted_lst = ", ".join([f"{x:.1f}" for x in lst])
        print(f'Add Vector is : [{formatted_lst}]')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        lst: list[float] = []
        for i in range(len(V1)):
            lst.append(V1[i] - V2[i])
        formatted_lst = ", ".join([f"{x:.1f}" for x in lst])
        print(f'Sous Vector is : [{formatted_lst}]')


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
