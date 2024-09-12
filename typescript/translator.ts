type Alphabet = { [key: string]: string };

/**
 * A mapping of English letters, numbers, and special characters to their Braille representations.
 *
 * Each Braille character is represented as a 6-character string where:
 * - 'O' represents a raised dot.
 * - '.' represents a flat (unraised) dot.
 *
 * Special keys:
 * - "cap" represents the Braille capitalization symbol.
 * - "num" represents the Braille number symbol.
 *
 * Example:
 * - 'a' maps to "O....." (Braille for the letter 'a').
 * - '1' maps to "O....." (Braille for the number '1').
 *
 * @type {Alphabet}
 */
const brailleAlphabet: Alphabet = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  "0": ".OOO..",
  " ": "......",
  cap: ".....O",
  num: ".O.OOO",
};

/**
 * A reverse mapping of Braille representations to their corresponding English letters, numbers, and special characters.
 *
 * Each Braille character (6-character string of 'O' and '.') is mapped to its corresponding
 * English letter or number.
 *
 * Example:
 * - "O....." maps to 'a' (Braille for the letter 'a').
 * - "O....." also maps to '1' when in number mode.
 *
 * This mapping is used for translating Braille back into English.
 *
 * @type {Alphabet}
 */
const englishAlphabet: Alphabet = Object.fromEntries(
  Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

/**
 * Determines if the given input string is written in Braille.
 *
 * Braille is represented by a series of 'O' (for raised dots) and '.' (for flat dots).
 * This function checks if the input consists only of these characters.
 *
 * @param {string} input - The input string to check.
 * @returns {boolean} Returns true if the input is a Braille string (only contains 'O' and '.'), otherwise false.
 */
const isBraille = (input: string): boolean => /^[O.]+$/.test(input);

/**
 * Translates a Braille string into its corresponding English representation using reduce.
 *
 * The Braille input is expected to be a series of 6-character Braille cells
 * (each represented by 'O' for raised dots and '.' for flat dots).
 * The function handles special Braille symbols for capitalization and numbers.
 *
 * @param {string} braille - The Braille string to translate.
 * @returns {string} The English translation of the Braille input.
 */
const translateToEnglish = (braille: string): string => {
  let isCapital = false;
  let isNumberMode = false;

  return (
    braille.match(/.{6}/g)?.reduce((result, brailleChar) => {
      if (brailleChar === brailleAlphabet["cap"]) {
        isCapital = true;
        return result;
      }

      if (brailleChar === brailleAlphabet["num"]) {
        isNumberMode = true;
        return result;
      }

      const englishChar = englishAlphabet[brailleChar] || "";

      if (isNumberMode) {
        if (englishChar === " ") {
          isNumberMode = false; // Turn off number mode after a space
        } else if (/[a-j]/.test(englishChar)) {
          // Translate letters 'a' to 'j' as numbers '1' to '0'
          const number = "1234567890"["abcdefghij".indexOf(englishChar)];
          return result + number;
        }
      }

      if (isCapital) {
        isCapital = false;
        return result + englishChar.toUpperCase();
      }

      return result + englishChar;
    }, "") || ""
  );
};

/**
 * Translates an English string into its corresponding Braille representation using reduce.
 *
 * The English input can include letters, numbers, spaces, and capitalization.
 * This function adds the appropriate Braille indicators for capitalization and numbers.
 *
 * @param {string} english - The English string to translate.
 * @returns {string} The Braille translation of the English input.
 */
const translateToBraille = (english: string): string => {
  let isNumberMode = false;

  return [...english].reduce((result, char) => {
    const lowerChar = char.toLowerCase();

    if (char !== lowerChar) {
      result += brailleAlphabet["cap"];
    }

    if (/[0-9]/.test(char) && !isNumberMode) {
      result += brailleAlphabet["num"];
      isNumberMode = true;
    } else if (!/[0-9]/.test(char)) {
      isNumberMode = false;
    }

    return result + (brailleAlphabet[lowerChar] || "");
  }, "");
};

/**
 * Translates an input string between English and Braille.
 * @param {string} input - The string to be translated. Can be either an English phrase or Braille.
 * @returns {string} The translated string, either Braille or English, depending on the input.
 */
const translate = (input: string): string => {
  if (isBraille(input)) {
    return translateToEnglish(input);
  }

  return translateToBraille(input);
};

// Get the user input
const input = process.argv.slice(2).join(" ");

// Output the translation
console.log(translate(input));
