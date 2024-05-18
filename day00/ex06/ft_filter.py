def ft_filter(fun, sequence):
    '''ft_filter(function or None, iterable) --> ft_filter object

    Return an iterator yielding those items of iterable for
     which function(item) is true.
     If function is None, return the items that are true.'''
    return iter([c for c in sequence if fun(c)])


def test_fun(variable):
    '''test_fun returns true or false if the
    variable is in this list ['a', 'e', 'i', 'o', 'u'] or not'''
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


def main():
    '''main function'''
    print(ft_filter(test_fun, ['a', 'b', 'c', 'd', 'e']))
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
