# Dictionary mapping codes to letters (reverse of the codes dictionary in the FileEncryption.py program)
reverse_codes_dict = {'%': 'A', '9': 'a', '@': 'B', '#': 'b', '$': 'C', '*': 'c', '!': 'D', '1': 'd', '&': 'E', '2': 'e',
                 '?': 'F', '3': 'f', '^': 'G', '4': 'g', '(': 'H', '5': 'h', ')': 'I', '6': 'i', '-': 'J', '7': 'j',
                 '_': 'K', '8': 'k', '+': 'L', '=': 'l', '[': 'M', '{': 'm', ']': 'N', '}': 'n', '~': 'O', ';': 'o',
                 '<': 'P', '>': 'p', '|': 'R', '0': 'r', 'Q': 'S', 'q': 's', 't': 'T', 'T': 't', 'u': 'U', 'U': 'u',
                 'v': 'V', 'V': 'v', 'w': 'W', 'W': 'w', 'x': 'X', 'X': 'x', 'y': 'Y', 'Y': 'y', 'z': 'Z', 'Z': 'z'}

#Path for the Encrypted file created using the FileEncryption.py program.
encrypted_file = 'encrypted.txt'

#Reading the encrypted file in READ Mode
file = open(encrypted_file, 'r')
encrypted_contents = file.read()

#Decrypting the encrypted contents
decrypted_contents = ''
for char in encrypted_contents:
    if char in reverse_codes_dict:
        decrypted_contents += reverse_codes_dict[char]
    else:
        decrypted_contents += char

print(decrypted_contents)


'''
Output of this program is matching with the original file info_security.txt

Employee behavior can have a big impact on information security in organizations.
Cultural concepts can help different segments of the organization work effectively
or work against effectiveness towards information security within an organization.
Exploring the Relationship between Organizational Culture and Information Security 
Culture provides the following definition of information security culture: ISC is 
the totality of patterns of behavior in an organization that contribute to the 
protection of information of all kinds.
'''