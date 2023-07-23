#Creating a empty Dictionary 
word_frequency = {}

infile = open('sometext.txt', 'r')
# Read the contents of the file in READ Mode
contents = infile.read()

# Remove punctuation marks and convert to the entire contents into lowercase
contents = contents.lower()
contents_updated = contents.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace('-', ' ')


# Split the contents into individual words
words = contents_updated.split()

#print(words)

# Count the frequency of each word
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

#print(word_frequency.items())

# Displaying the frequency of each word within the dictionary created
for word, frequency in word_frequency.items():
    print("The frequency of the word, ", f'{word} : {frequency}')