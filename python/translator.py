import sys

class Translations: 
    BRAILLE_CHARACTER_LENGTH = 6

    english_to_braille = {
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
        'capital': '.....O',
        'number': '.O.OOO',
        ' ': '......'
    }
    braille_to_english_alphabet = {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z'
    }
    braille_to_english_num = {
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9',
        '.OOO..': '0'
    }
    braille_to_english_action = {
        '.....O': 'capital',
        '.O.OOO': 'number',
        '......': ' '
    }
class Translator():
    translations = Translations()

    def is_braille(self, text):
        return all(c in 'O.' for c in text)

    def translate_braille(self, text):
        translated = []
        capital = False
        num = False

        for i in range(0, len(text), self.translations.BRAILLE_CHARACTER_LENGTH):
            braille_char = text[i:i + self.translations.BRAILLE_CHARACTER_LENGTH]

            if braille_char in self.translations.braille_to_english_action:
                action = self.translations.braille_to_english_action[braille_char]
                if action == 'capital':
                    capital = True
                elif action == 'number':
                    num = True
                else:
                    num = False
                    translated.append(' ')
            else:
                if num:
                    translated.append(self.translations.braille_to_english_num[braille_char])
                else:
                    letter = self.translations.braille_to_english_alphabet[braille_char]
                    translated.append(letter.upper() if capital else letter)
                    capital = False

        return ''.join(translated)

    def translate_english(self, text):
        translated = []
        words = text.split(' ')

        for word in words:
            if word.isdigit():
                translated.append(self.translations.english_to_braille['number'])
                for num in word:
                    translated.append(self.translations.english_to_braille[num])
            else:
                for char in word:
                    if char.isupper():
                        translated.append(self.translations.english_to_braille['capital'])
                    translated.append(self.translations.english_to_braille[char.lower()])
            translated.append(self.translations.english_to_braille[' '])

        return ''.join(translated[:-1])

    def translate(self, text):
        if self.is_braille(text):
            return self.translate_braille(text)
        else:
            return self.translate_english(text)

if __name__ == "__main__":
    translator = Translator()
    text = ' '.join(sys.argv[1:])
    print(translator.translate(text), end='')

