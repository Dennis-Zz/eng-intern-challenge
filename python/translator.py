import sys

class BrailleTranslator:
    def __init__(self):
        self.letters_to_braille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
            'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
            'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
            'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
            'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
            'y': 'OO.OOO', 'z': 'O..OOO',
        }

        self.numbers_to_braille = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
            '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
            '9': '.OO...', '0': '.OOO..',
        }

        self.punctuation_to_braille = {
            '.': '.O..OO', ',': '.O....', '?': '.O.OO.', '!': '.OO.O.', 
            ':': 'OO....', ';': 'O.O...', '-': '......', '/': 'O.O...', 
            '<': 'O..OO.', '>': '.OOO.O', '(': 'OO.OO.', ')': '.OO.OO',
        }

        self.special_symbols = {
            'cap_follows': '.....O', 'num_follows': '.O.OOO', 'dec_follows': '.O...O', ' ': '......',
        }

        # Inverse mappings for braille to english
        self.braille_to_letters = {braille: letter for letter, braille in self.letters_to_braille.items()}
        self.braille_to_numbers = {braille: letter for letter, braille in self.numbers_to_braille.items()}
        self.braille_to_punctuation = {braille: letter for letter, braille in self.punctuation_to_braille.items()}
