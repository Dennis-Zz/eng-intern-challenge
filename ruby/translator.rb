BRAILLE_TO_ENGLISH = { 'O.....' => 'a',
                       'O.O...' => 'b',
                       'OO....' => 'c',
                       'OO.O..' => 'd',
                       'O..O..' => 'e',
                       'OOO...' => 'f',
                       'OOOO..' => 'g',
                       'O.OO..' => 'h',
                       '.O.O..' => 'i',
                       '.OOO..' => 'j',
                       'O...O.' => 'k',
                       'O.O.O.' => 'l',
                       'OO..O.' => 'm',
                       'OO.OO.' => 'n',
                       'O..OO.' => 'o',
                       'OOO.O.' => 'p',
                       'OOOO.O' => 'q',
                       'O.OOO.' => 'r',
                       '.OO.O.' => 's',
                       '.OOOO.' => 't',
                       'O...OO' => 'u',
                       'O.O.OO' => 'v',
                       '.OOO.O' => 'w',
                       'OO..OO' => 'x',
                       'OO.OOO' => 'y',
                       'O..OOO' => 'z',
                       '......' => ' ' }.freeze
ENGLISH_TO_BRAILLE = BRAILLE_TO_ENGLISH.invert
BRAILLE_TO_NUMBERS = { 'O.....' => '1',
                       'O.O...' => '2',
                       'OO....' => '3',
                       'OO.O..' => '4',
                       'O..O..' => '5',
                       'OOO...' => '6',
                       'OOOO..' => '7',
                       'O.OO..' => '8',
                       '.O.O..' => '9',
                       '.OOO..' => '0' }.freeze
NUMBERS_TO_BRAILLE = BRAILLE_TO_NUMBERS.invert
NUMBER_FOLLOWS = '.O.OOO'.freeze
CAPITAL_FOLLOWS = '.....O'.freeze

def translate_to_braille(text)
  result = ''
  number_mode = false
  text.chars.each do |char|
    if char.match?(/\d/)
      unless number_mode
        result << NUMBER_FOLLOWS
        number_mode = true
      end
      result << NUMBERS_TO_BRAILLE[char]
    elsif char == ' '
      result << ENGLISH_TO_BRAILLE[char]
      number_mode = false
    else

      result << if char == char.upcase && ENGLISH_TO_BRAILLE[char.downcase]
                  CAPITAL_FOLLOWS + ENGLISH_TO_BRAILLE[char.downcase]
                else
                  ENGLISH_TO_BRAILLE[char]
                end
    end
  end
  result
end

