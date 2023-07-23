# Dictionary is created to store the codes
codes_dict = {'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '*', 'D': '!', 'd': '1', 'E': '&', 'e': '2',
         'F': '?', 'f': '3', 'G': '^', 'g': '4', 'H': '(', 'h': '5', 'I': ')', 'i': '6', 'J': '-', 'j': '7',
         'K': '_', 'k': '8', 'L': '+', 'l': '=', 'M': '[', 'm': '{', 'N': ']', 'n': '}', 'O': '~', 'o': ';',
         'P': '<', 'p': '>', 'R': '|', 'r': '0', 'S': 'Q', 's': 'q', 'T': 't', 't': 'T',
         'U': 'u', 'u': 'U', 'V': 'v', 'v': 'V', 'W': 'w', 'w': 'W', 'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y',
         'Z': 'z', 'z': 'Z'}

input_file = 'info_security-1.txt'
output_file = 'encrypted.txt'

#Opening the input file in READ Mode
file = open(input_file, 'r')
contents = file.read()

encrypted_contents = ''
for char in contents:
    if char in codes_dict:
        encrypted_contents += codes_dict[char]
    else:
        encrypted_contents += char

final_output = open(output_file, 'w')

final_output.write(encrypted_contents)

print(f"Encryption completed. The encrypted contents are saved in '{output_file}'.")