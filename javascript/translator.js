// Dictionaries for value mapping 
const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '..OO.O', ',': '..O...', '!': '..OOO.', '?': '..O.O.', '-': '....O.',
    "'": '....O.', ':': 'O.OO.O', ';': 'O.OO..', '/': '.O..O.', '(': '.O.OO.', ')': '.O.OO.',
    'CAP': '.....O' 
  };

  // Reverse dictionary values for braille to English 
  const brailleToEnglish = Object.fromEntries(Object.entries(englishToBraille).map(([key, value]) => [value, key]));

  // Main function

  // Part 1 : English or Braille
  function isBraille(input){
    return /^[.O\s]+$/.test(input) && input.length % 6 === 0;
  }

  // Part 2: Translation
