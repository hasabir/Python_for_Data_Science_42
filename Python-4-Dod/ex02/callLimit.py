def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(f'Error: {function} call too many times')
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
