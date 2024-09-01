import sys

from bidirectional_dict import BidirectionalDict
# Constants

# NOTE: Thought about using a biderectional 
# ENGLISH_TO_BRAILLE = {
#     "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
#     "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
#     "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
#     "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
#     "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
#     "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....",
#     "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
#     "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"
# }

# BRAILLE_TO_ENGLISH = {
#     "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
#     "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
#     "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
#     "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
#     "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
#     "O..OOO": "z", "O.....": "1", "O.O...": "2", "OO....": "3",
#     "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7",
#     "O.OO..": "8", ".OO...": "9", ".OOO..": "0", "......": " "
# }

# Constants
CAPITAL_PREFIX = "O.OOOO"
NUMBER_PREFIX = ".O.OOO"
SPACE = "......" # ' '

def create_braille_alphabet_bidict():
    braille_alphabet_bidict = BidirectionalDict()
    braille_alphabet_bidict.add("a", "O.....")
    braille_alphabet_bidict.add("b", "O.O...")
    braille_alphabet_bidict.add("c", "OO....")
    braille_alphabet_bidict.add("d", "OO.O..")
    braille_alphabet_bidict.add("e", "O..O..")
    braille_alphabet_bidict.add("f", "OOO...")
    braille_alphabet_bidict.add("g", "OOOO..")
    braille_alphabet_bidict.add("h", "O.OO..")
    braille_alphabet_bidict.add("i", ".OO...")
    braille_alphabet_bidict.add("j", ".OOO..")
    braille_alphabet_bidict.add("k", "O...O.")
    braille_alphabet_bidict.add("l", "O.O.O.")
    braille_alphabet_bidict.add("m", "OO..O.")
    braille_alphabet_bidict.add("n", "OO.OO.")
    braille_alphabet_bidict.add("o", "O..OO.")
    braille_alphabet_bidict.add("p", "OOO.O.")
    braille_alphabet_bidict.add("q", "OOOOO.")
    braille_alphabet_bidict.add("r", "O.OOO.")
    braille_alphabet_bidict.add("s", ".OO.O.")
    braille_alphabet_bidict.add("t", ".OOOO.")
    braille_alphabet_bidict.add("u", "O...OO")
    braille_alphabet_bidict.add("v", "O.O.OO")
    braille_alphabet_bidict.add("w", ".OOO.O")
    braille_alphabet_bidict.add("x", "OO..OO")
    braille_alphabet_bidict.add("y", "OO.OOO")
    braille_alphabet_bidict.add("z", "O..OOO")
    return braille_alphabet_bidict

def create_braille_numerical_bidict():
    braille_numerical_bidict = BidirectionalDict()
    braille_numerical_bidict.add("1", "O.....")
    braille_numerical_bidict.add("2", "O.O...")
    braille_numerical_bidict.add("3", "OO....")
    braille_numerical_bidict.add("4", "OO.O..")
    braille_numerical_bidict.add("5", "O..O..")
    braille_numerical_bidict.add("6", "OOO...")
    braille_numerical_bidict.add("7", "OOOO..")
    braille_numerical_bidict.add("8", "O.OO..")
    braille_numerical_bidict.add("9", ".OO...")
    braille_numerical_bidict.add("0", ".OOO..")
    return braille_numerical_bidict

'''
In Braille Alphabet in the technical requirements it does not state that '.' can be a vaild alphabet input in this program

Vaild Braille Alphabet are:
    1. Letters a through z(lowercase and uppercase)
    2. Numbers 0 through 9
    3. Spaces

This means if '.' is found in a string it is a braille and not a vaild braille alphabet
'''
def is_braille(text):
    for c in text:
        if c == '.':
            return True
    return False

def vaild_braille(text):
    return len(text) % 6 == 0

# Gets input from terminal
def get_system_arguments(args):
    text = ""
    for i in range(1,len(args) - 1):
        text += args[i] + " "
    text += args[len(args) - 1]

    return text

# def convert_brallie_to_english(text):



# Runs the Translator
def main():
    # text = get_system_arguments(sys.argv)
    # print(text)
    # if is_braille(text) and vaild_braille(text):
    #     print(convert_brallie_to_english(text))
    # print("RAN")
    braille_alphabet_bidict = create_braille_alphabet_bidict()
    braille_numerical_bidict = create_braille_numerical_bidict()
    print(braille_alphabet_bidict.get('a'))
    print(braille_alphabet_bidict.get_by_value('O.O...'))

if __name__ == "__main__":
    main() 