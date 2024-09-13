import sys

braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital_follows': '.....O',
    'decimal_follows': '.O...O',
    'number_follows': '.O.OOO',
    ' ': '......',
    # '.': '..OO.O',
    # ',': '..O.OO',
    # '!': '..OOO.',
    # ':': '..O.O.',
    # ';': '..O.O.',
    # '-': '....OO',
    # '/': '.O..O.',
    # '<': '.OO..O',
    # '>': 'O..OO.',
    # '(': 'O.O..O',
    # ')': '.O.OO.',
}

braille_numbers = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    ' ': '......',
}

# Defining some functions!
def check_braille(string):
    '''Check if given string is a braille text'''
    symbols = {'.', 'O'}
    if len(string) % 6 != 0:
        return False
    for char in string:
        if char not in symbols:
            return False
    return True

# for value in braille.values():
#     assert check_braille(value)
# for value in braille_numbers.values():
#     assert check_braille(value)

# *********************************
# Skipping file name
text = sys.argv[1:]

# English -> Braille
if len(text) > 1 or check_braille(text[0]) is False:
    for char in ' '.join(text):
        if char.isupper():
            sys.stdout.write(braille['capital_follows'])
            sys.stdout.write(braille[char.lower()].upper())
        elif char.isdigit():
            sys.stdout.write(braille['number_follows'])
            sys.stdout.write(braille_numbers[char])
        else:
            sys.stdout.write(braille[char])

# Braille -> English
else:
    # Flip dictionnary
    text = text[0]
    braille = {braille: letter for letter, braille in braille.items()}
    braille_numbers = {braille: letter for letter, braille in braille.items()}
    # Writing numbers state
    write_numbers = False
    a = 0
    b = 6
    while b < len(text):
        braille_string = text[a:b]
        # Numbers
        if write_numbers is True:
            output = braille_numbers[braille_string]
            sys.stdout.write(braille_numbers[braille_string])
            if output == ' ':
                write_numbers = False
        # Checking for number_follows
        elif braille[braille_string] == 'number_follows':
            write_numbers = True
        elif braille[braille_string] == 'capital_follows':
            a += 6
            b += 6
            sys.stdout.write(braille[text[a:b]])
            continue
        else:
            sys.stdout.write(braille[braille_string])

        a += 6
        b += 6
            

