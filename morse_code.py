morse_code_dict= {
    "a": ". _",
    "b": "_ . . .",
    "c": "_ . _ .",
    "d": "_ . .",
    "e": ".",
    "f": ". . _ .",
    "g": "_ _ .",
    "h": ". . . .",
    "i": ". .",
    "j": ". _ _ _",
    "k": "_ . _",
    "l": ". _ . .",
    "m": "_ _",
    "n": "_ .",
    "o": "_ _ _",
    "p": ". _ _ .",
    "q": "_ _ . _",
    "r": ". _ .",
    "s": ". . .",
    "t": "_",
    "u": ". . _",
    "v": ". . . _",
    "w": ". _ _",
    "x": "_ . . _",
    "y": "_ . _ _",
    "z": "_ _ . ."
    }

sentence = input("Enter your sentence which will be converted to morse code: ")
print(sentence)
# morse code sentence that will be created after user types the sentence in the console
morse_code_sentence = ""
for letter in sentence:
    # if there is a space between words I am marking it as '/'
    if letter == " ":
        # checking if the previous character is '*' as we are adding the '*' after every letter
        morse_code_sentence = morse_code_sentence[:-1]
        morse_code_sentence += "/"
    # checking if the letter is in our dictionary, if it is we will add letter morse code to our morse_code_sentence
    if letter in morse_code_dict:
        morse_code_sentence += morse_code_dict[letter] + "*"

# in the end checking if the last character is '*' or '/' and removing it rom the morse code sentence
if morse_code_sentence[-1] == "*" or morse_code_sentence[-1] == "/":
    morse_code_sentence = morse_code_sentence[:-1]
print(morse_code_sentence)

