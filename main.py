# Take a string input and return the string as morse code.

morse_code_alphanum = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


input_str = input('Enter a string to be converted to morse code: ')

input_str = input_str.upper()
output_str = ''

# Run through the string, turning each character into morse code.
for i in input_str:
    if i in morse_code_alphanum:
        output_str += morse_code_alphanum[i] + ' '
    elif i == ' ':
        output_str += '\n'

print(output_str)