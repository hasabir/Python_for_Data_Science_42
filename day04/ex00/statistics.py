from typing import Any, Callable, Dict, List


class Statistic():
    @staticmethod
    def mean(args):
        return sum(args)/len(args)

    @staticmethod
    def median(args):
        n = int(len(args)/2)
        list = sorted(args)
        return list[n] if len(args) % 2 != 0 else list[n] + (list[n] - 1)

    @staticmethod
    def quartile(args):
        lower_quartile = sorted(args)[int(len(args)/4)]
        upper_quartile = sorted(args)[int(3 * len(args)/4)]
        return f"[{lower_quartile:.1f}, {upper_quartile:.1f}]"

    @staticmethod
    def var(args):
        stock = []
        for arg in args:
            stock.append((arg - Statistic.mean(args)) ** 2)
        return sum(stock)/len(args)

    @staticmethod
    def std(args):
        return Statistic.var(args)**(1/2)

    @classmethod
    def get_stat_function(cls, name: str) -> Callable[[List[float]], Any]:
        functions: Dict[str, Callable[[List[float]], Any]] = {
            "mean": cls.mean,
            "median": cls.median,
            "quartile": cls.quartile,
            "var": cls.var,
            "std": cls.std
        }
        return functions.get(name)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for kwarg in kwargs:
        if not args:
            print('ERROR')
        else:
            fn = Statistic.get_stat_function(kwargs[kwarg])
            if fn:
                print(f"{kwargs[kwarg]} : {fn(args)}")


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
