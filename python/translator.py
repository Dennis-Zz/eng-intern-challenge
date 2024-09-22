import sys

braille_to_eng = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",
    ".O.OO.": ")", "......": " "
}

braille_to_eng_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}

braille_to_eng_inst = {
    ".....O": "cap",
    ".O...O": "dec",
    ".O.OOO": "num"
}

eng_to_braille = {value: key for key, value in braille_to_eng.items()}
eng_to_braille_num = {value: key for key, value in braille_to_eng_num.items()}
eng_to_braille_inst = {value: key for key, value in braille_to_eng_inst.items()}


def translate(input_args):
    if len(input_args) > 1:
        eng_str = " ".join(input_args)
        print(trans_eng_to_braille(eng_str))
    elif any(char not in [".", "O"] for char in input_args[0]):
        print(trans_eng_to_braille(input_args[0]))
    else:
        print(trans_braille_to_eng(input_args[0]))


def trans_braille_to_eng(braille_str):
    braille_unit_arr = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    capitalize = "OFF"
    number = "OFF"
    decimal = "OFF"
    eng_string = ""

    for braille_unit in braille_unit_arr:
        # If braille_unit is an instruction:
        if braille_unit in braille_to_eng_inst:
            if braille_to_eng_inst[braille_unit] == "cap":
                capitalize = "ON"
            # elif braille_to_eng_inst[braille_unit] == "dec":
            #     eng_string += "."
            elif braille_to_eng_inst[braille_unit] == "num":
                number = "ON"
        else:
            # if space, add space to string, change number to "OFF"
            if braille_to_eng[braille_unit] == " ":
                eng_string += " "
                number = "OFF"
            # if capital switch on
            elif capitalize == "ON":
                eng_string += braille_to_eng[braille_unit].upper()
                capitalize = "OFF"
            elif number == "ON":
                # If is a decimal point within a number
                if braille_unit == eng_to_braille["."]:
                    eng_string += braille_to_eng[braille_unit]
                else:
                    eng_string += braille_to_eng_num[braille_unit]
            else:
                eng_string += braille_to_eng[braille_unit]

    return eng_string


def trans_eng_to_braille(eng_string):
    braille_str = ""
    num = "OFF"

    for char in eng_string:
        if char.isupper():
            braille_str += eng_to_braille_inst["cap"]
            braille_str += eng_to_braille[char.lower()]
        elif char.isdigit():
            if num == "OFF":
                braille_str += eng_to_braille_inst["num"]
                num = "ON"
            braille_str += eng_to_braille_num[char]
        elif char == " ":
            num = "OFF"
            braille_str += eng_to_braille[char]
        else:
            braille_str += eng_to_braille[char]

    return braille_str

if __name__ == "__main__":
    input_str = sys.argv[1:]
    translate(input_str)

