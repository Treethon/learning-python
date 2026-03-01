## Run the script to generate a 16 digit password.  Can be improved to make generated password 
## have at least 1 number, letter, and symbol. Use .join() method on string.
import random

SYMBOLS = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "/", ".",
           ",", "<", ">", "?", ";", ":", "[", "]", "{", "}")
NUMBERS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
LETTERS = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
PW_LENGTH = 16
selected_chars = []
password = ""
has_symbol = False
has_number = False
has_letter = False

while len(selected_chars) < 16:
    selected_str = random.randint(0,2) ## Defines if indexed place in string is a symbol, number, or letter.
    if selected_str == 0:
        selected_chars.append(random.choice(SYMBOLS))
        has_symbol = True
    elif selected_str == 1:
        selected_chars.append(random.choice(NUMBERS))
        has_number = True
    else:
        selected_chars.append(random.choice(LETTERS))
        has_letter = True
password = "".join(selected_chars)

print(password)