import sys as sys


def main():
    '''	This program calculate the characters of your string,
    upper-case characters, lower-case characters,
     punctuation characters, digits and spaces'''
    lines = ''
    try:
        if (len(sys.argv) > 2):
            raise AssertionError('number of arguments incorrect')
        if len(sys.argv) == 1:
            for line in sys.stdin:
                try:
                    lines = line
                except EOFError:
                    break
        else:
            lines = sys.argv[1]
        print('The text contains ', len(lines), ' characters:')
        print(sum(c.isupper() for c in lines), ' upper letters')
        print(sum(c.islower() for c in lines), ' lower letters')
        print(sum(not c.isalnum() and c != ' ' and c != '\n' for c in lines),
               ' punctuation marks')
        print(lines.count(' '), ' spaces')
        print(sum(c.isdigit() for c in lines), ' digits')
    except AssertionError as e:
        print('AssertionError: ', e)


if __name__ == "__main__":
    main()
