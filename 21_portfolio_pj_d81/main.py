# Program that takes any String input and converts it into Morse Code.
# NOTE: To decode type " " between each morse code character and type " " + ">" + " " to express space. 

latin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@', 'End of work', 'Error', 'Invatation to transmit', 'Starting Signal', 'New Page Signal', 'Understood', 'Wait']

morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '>', '.-.-.-', '--.--', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.', '...-.-', '........', '-.-', '-.-.-', '...-.', '.-...']

def encode():
    text_str = input("Input text: ")
    encoded = ''
    for char in text_str:
        if morse_code[latin.index(char.lower())] == '>':
            continue
        else:
            encoded += morse_code[latin.index(char.lower())]
            encoded += " "

    print(encoded)

def decode():
    morse_encoded = input('Input morse code: ')
    decoded = ''
    code_letters = morse_encoded.split(' ')
    for code in code_letters:
        decoded += latin[morse_code.index(code)]

    print(decoded)

choose_func = input('Type "d" to decode, "e" to encode: ')
if choose_func == 'd':
    decode()
else:
    encode()