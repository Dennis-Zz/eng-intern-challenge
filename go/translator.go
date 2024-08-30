package main

import (
	"fmt"
	"os"
	"strings"
)

// English to Braille maps
var englishToBraille = map[string]string{
	"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
	"f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
	"k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
	"p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
	"u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
	"z": "O..OOO",
	" ": "......", "cap": ".....O",  
}

var numberToBraille = map[string]string{
	"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
	"6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

// Braille to English maps
var brailleToEnglish = map[string]string{
	"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
	"OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
	"O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
	"OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
	"O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
	"O..OOO": "z",
	"......": " ",
}

var brailleToNumbers = map[string]string{
	"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
	"OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

// Translate function
func translateText(input string) string {
	var result strings.Builder

	if !strings.ContainsAny(input, "O.") {
		// Translate English to Braille
		for _, ch := range input {
			charStr := string(ch)
			if ch >= 'A' && ch <= 'Z' {
				result.WriteString(englishToBraille["cap"])
				result.WriteString(englishToBraille[strings.ToLower(charStr)])
			} else if ch >= 'a' && ch <= 'z' {
				result.WriteString(englishToBraille[charStr])
			} else if ch >= '0' && ch <= '9' {
				result.WriteString(".O.OOO") // Number indicator
				result.WriteString(numberToBraille[charStr])
			} else {
				// Handle other characters (punctuation)
				result.WriteString(englishToBraille[" "])
			}
		}
		return result.String()
	}

	// Translate Braille to English
	i := 0
	isCap := false
	isNumber := false

	for i < len(input) {
		if i+6 <= len(input) {
			brailleChar := input[i : i+6]

			if brailleChar == ".....O" {
				// Capitalization indicator
				isCap = true
				i += 6
				continue
			} else if brailleChar == ".O.OOO" {
				// Numbers indicator
				isNumber = true
				i += 6
				continue
			}

			var englishChar string
			if isNumber {
				englishChar = brailleToNumbers[brailleChar]
			} else {
				englishChar = brailleToEnglish[brailleChar]
			}

			if englishChar != "" {
				if isCap {
					englishChar = strings.ToUpper(englishChar)
					isCap = false
				}
				result.WriteString(englishChar)
			} else {
				// Handle invalid or unknown Braille sequences
				result.WriteString("?")
			}

			// Reset number after a space
			if brailleChar == "......" {
				isNumber = false
			}

			i += 6
		} else {
			// Handle cases where there isn't a full 6-character Braille sequence
			result.WriteString("?")
			i += 6
		}
	}

	return result.String()
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide input text.")
		return
	}

	input := os.Args[1]
	output := translateText(input)
	fmt.Println(output)
}
//To test the following in the terminal
//go run translator.go "test case"    