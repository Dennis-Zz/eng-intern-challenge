// Capital, Number, and Decimal Follower
const CAPITAL : string = ".....O";
const NUMBER : string = ".O.OOO";
const SPACE : string = "......";


// Set up dictionary between Letter and Braille
const LETTER_TO_BRAILLE : Map<string, string> = new Map<string, string>([
    ["a", "O....."], ["b", "O.O..."], ["c", "OO...."], ["d", "OO.O.."], ["e", "O..O.."],
    ["f", "OOO..."], ["g", "OOOO.."], ["h", "O.OO.."], ["i", ".OO..."], ["j", ".OOO.."],
    ["k", "O...O."], ["l", "O.O.O."], ["m", "OO..O."], ["n", "OO.OO."], ["o", "O..OO."],
    ["p", "OOO.O."], ["q", "OOOOO."], ["r", "O.OOO."], ["s", ".OO.O."], ["t", ".OOOO."],
    ["u", "O...OO"], ["v", "O.O.OO"], ["w", ".OOO.O"], ["x", "OO..OO"], ["y", "OO.OOO"],
    ["z", "O..OOO"]
]);
const BRAILLE_TO_LETTER : Map<string, string> = new Map<string, string>();
LETTER_TO_BRAILLE.forEach((value : string, key : string) => BRAILLE_TO_LETTER.set(value, key));

// Set up dictionary between Number and Braille
const NUMBER_TO_BRAILLE = new Map<string, string>([
    ["1", "O....."], ["2", "O.O..."], ["3", "OO...."], ["4", "OO.O.."], ["5", "O..O.."],
    ["6", "OOO..."], ["7", "OOOO.."], ["8", "O.OO.."], ["9", ".OO..."], ["0", ".OOO.."]
]);
const BRAILLE_TO_NUM = new Map<string, string>();
NUMBER_TO_BRAILLE.forEach((value, key) => BRAILLE_TO_NUM.set(value, key));


// Check the input type is English or not
function isEnglish(input: string): Promise<boolean> {
    return new Promise((resolve, reject) => {
        try {
            for (let char of input) {
                // If not "O" or ".", must be English
                if (char !== 'O' && char !== '.') {
                    resolve(true); // It's English
                    return;
                }
            }
            resolve(false); // It's Braille
        } catch (error: any) {
            reject(new Error(`Error in isEnglish: Unable to determine the language. ${error.message}`));
        }
    });
}

function englishToBraille(input: string): Promise<string> {
    return new Promise((resolve, reject) => {
        try {
            let numberFollow: boolean = false;
            let braille: string = "";

            Array.from(input).forEach((char: string) => {
                if (/[a-z]/.test(char)) {
                    numberFollow = false;
                    braille += LETTER_TO_BRAILLE.get(char);
                } else if (/[A-Z]/.test(char)) {
                    numberFollow = false;
                    braille += CAPITAL + LETTER_TO_BRAILLE.get(char.toLowerCase())!;
                } else if (char === " ") {
                    braille += SPACE;
                    numberFollow = false;
                } else if (/[0-9]/.test(char) && !numberFollow) {
                    braille += NUMBER + NUMBER_TO_BRAILLE.get(char)!;
                    numberFollow = true;
                } else {
                    braille += NUMBER_TO_BRAILLE.get(char)!;
                }
            });
            resolve(braille); // Resolve the promise with the braille result
        } catch (error: any) {
            reject(new Error(`Error in englishToBraille: Failed to convert English to Braille. ${error.message}`));
        }
    });
}

function brailleToEnglish(input: string): Promise<string> {
    return new Promise((resolve, reject) => {
        try {
            let english: string = "";
            let numberFollows: boolean = false;
            let capitalFollows: boolean = false;

            // Split the input into an array of Braille characters (each 6 characters long)
            const braille: string[] = input.match(/.{1,6}/g) || [];

            braille.forEach(brailleChar => {
                // Handle Followers and Space Case
                if (brailleChar === NUMBER) {
                    numberFollows = true;
                    return;
                } else if (brailleChar === CAPITAL) {
                    capitalFollows = true;
                    return;
                } else if (brailleChar === SPACE) {
                    numberFollows = false;
                    english += " ";
                    return;
                }

                // Handle Normal Letter and Number Case
                if (capitalFollows) {
                    english += BRAILLE_TO_LETTER.get(brailleChar)?.toUpperCase();
                    capitalFollows = false;
                } else if (numberFollows) {
                    english += BRAILLE_TO_NUM.get(brailleChar)!;
                } else {
                    english += BRAILLE_TO_LETTER.get(brailleChar)!;
                }
            });

            resolve(english); // Resolve the promise with the English result
        } catch (error: any) {
            reject(new Error(`Error in brailleToEnglish: Failed to convert Braille to English. ${error.message}`));
        }
    });
}

function main(): void {
    const input = process.argv.slice(2).join(" ");

    isEnglish(input)
        .then(isEng => {
            if (isEng) {
                return englishToBraille(input);
            } else {
                return brailleToEnglish(input);
            }
        })
        .then(result => {
            console.log(result);
        })
        .catch(error => {
            console.error("Error:", error.message); // Catch any errors from the promises
        });
}

main();
