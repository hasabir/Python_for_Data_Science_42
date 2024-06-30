import sys as sys


def main():
    '''sos programme'''
    NESTED_MORSE = {
        ' ': "/", 'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError('the arguments are bad')
        codedMessage = ''
        for c in sys.argv[1]:
            if c.capitalize() in NESTED_MORSE:
                codedMessage += NESTED_MORSE.get(c.capitalize()) + ' '
            else:
                raise AssertionError('the arguments are bad')
        print(codedMessage.rstrip(codedMessage[-1]))
    except AssertionError as e:
        print("AssertionError: ", e)


if __name__ == "__main__":
    main()
