import getKeyFromValue from "./getKeyFromValue.js";

export const lettersDict = {
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
  " ": "......",
  ".": "..OO.O",
  ",": "..O...",
  ";": "..O.O.",
  ":": "..OO..",
  "!": "..OOO.",
  "?": "..O.OO",
  "(": "O.O..O",
  ")": ".O.OO.",
  "-": "....OO",
  "<": ".OO..O",
  ">": "O..OO.",
};

export const numbersDict = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
  ".": ".O...O",
};

export const modifiersDict = {
  capital: ".....O",
  number: ".O.OOO",
};

export const letterToBraille = (letter) => lettersDict[letter];
export const brailleToLetter = (braille) =>
  getKeyFromValue(lettersDict, braille);

export const numberToBraille = (number) => numbersDict[number];
export const brailleToNumber = (braille) =>
  getKeyFromValue(numbersDict, braille);

export const brailleToModifier = (braille) =>
  getKeyFromValue(modifiersDict, braille);
