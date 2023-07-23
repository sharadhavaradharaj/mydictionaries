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


'''
Output of the program

The frequency of the word,  no : 4
The frequency of the word,  one : 3
The frequency of the word,  is : 2
The frequency of the word,  unaware : 1      
The frequency of the word,  of : 8
The frequency of the word,  the : 16
The frequency of the word,  name : 1
The frequency of the word,  that : 1
The frequency of the word,  famous : 1       
The frequency of the word,  english : 1      
The frequency of the word,  shipowner : 1    
The frequency of the word,  cunard : 4       
The frequency of the word,  in : 7
The frequency of the word,  1840 : 1
The frequency of the word,  this : 5
The frequency of the word,  shrewd : 2       
The frequency of the word,  industrialist : 1
The frequency of the word,  founded : 1      
The frequency of the word,  a : 8
The frequency of the word,  postal : 1       
The frequency of the word,  service : 1      
The frequency of the word,  between : 1      
The frequency of the word,  liverpool : 1    
The frequency of the word,  and : 7
The frequency of the word,  halifax : 1
The frequency of the word,  featuring : 1
The frequency of the word,  three : 1
The frequency of the word,  wooden : 1
The frequency of the word,  ships : 5
The frequency of the word,  with : 5
The frequency of the word,  400 : 1
The frequency of the word,  horsepower : 2
The frequency of the word,  paddle : 2
The frequency of the word,  wheels : 2
The frequency of the word,  burden : 1
The frequency of the word,  1162 : 1
The frequency of the word,  metric : 2
The frequency of the word,  tons : 2
The frequency of the word,  eight : 2
The frequency of the word,  years : 3
The frequency of the word,  later : 1
The frequency of the word,  company's : 1
The frequency of the word,  assets : 2
The frequency of the word,  were : 1
The frequency of the word,  increased : 1
The frequency of the word,  by : 3
The frequency of the word,  four : 2
The frequency of the word,  650 : 1
The frequency of the word,  at : 2
The frequency of the word,  1820 : 1
The frequency of the word,  two : 2
The frequency of the word,  more : 2
The frequency of the word,  other : 1
The frequency of the word,  vessels : 1
The frequency of the word,  still : 2
The frequency of the word,  greater : 2
The frequency of the word,  power : 1
The frequency of the word,  tonnage : 1
The frequency of the word,  1853 : 1
The frequency of the word,  co : 1
The frequency of the word,  whose : 1
The frequency of the word,  mail : 1
The frequency of the word,  carrying : 1
The frequency of the word,  charter : 1
The frequency of the word,  had : 1
The frequency of the word,  just : 1
The frequency of the word,  been : 3
The frequency of the word,  renewed : 1
The frequency of the word,  successively : 1
The frequency of the word,  added : 1
The frequency of the word,  to : 3
The frequency of the word,  its : 3
The frequency of the word,  arabia : 1
The frequency of the word,  persia : 1
The frequency of the word,  china : 1
The frequency of the word,  scotia : 1
The frequency of the word,  java : 1
The frequency of the word,  russia : 1
The frequency of the word,  all : 2
The frequency of the word,  top : 1
The frequency of the word,  speed : 1
The frequency of the word,  after : 1
The frequency of the word,  great : 1
The frequency of the word,  eastern : 1
The frequency of the word,  biggest : 1
The frequency of the word,  ever : 1
The frequency of the word,  plow : 1
The frequency of the word,  seas : 1
The frequency of the word,  so : 3
The frequency of the word,  1867 : 1
The frequency of the word,  company : 2
The frequency of the word,  owned : 1
The frequency of the word,  twelve : 1
The frequency of the word,  propellers : 1
The frequency of the word,  if : 1
The frequency of the word,  i : 1
The frequency of the word,  give : 1
The frequency of the word,  these : 1
The frequency of the word,  highly : 1
The frequency of the word,  condensed : 1
The frequency of the word,  details : 1
The frequency of the word,  it : 1
The frequency of the word,  everyone : 1
The frequency of the word,  can : 2
The frequency of the word,  fully : 1
The frequency of the word,  understand : 1
The frequency of the word,  importance : 1
The frequency of the word,  maritime : 1
The frequency of the word,  transportation : 1
The frequency of the word,  known : 1
The frequency of the word,  world : 1
The frequency of the word,  over : 1
The frequency of the word,  for : 1
The frequency of the word,  management : 1
The frequency of the word,  transoceanic : 1
The frequency of the word,  navigational : 1
The frequency of the word,  undertaking : 1
The frequency of the word,  has : 1
The frequency of the word,  conducted : 1
The frequency of the word,  ability : 1
The frequency of the word,  business : 1
The frequency of the word,  dealings : 1
The frequency of the word,  have : 2
The frequency of the word,  crowned : 1
The frequency of the word,  success : 1
The frequency of the word,  twenty : 1
The frequency of the word,  six : 1
The frequency of the word,  made : 1
The frequency of the word,  2000 : 1
The frequency of the word,  atlantic : 1
The frequency of the word,  crossings : 1
The frequency of the word,  without : 1
The frequency of the word,  much : 1
The frequency of the word,  as : 2
The frequency of the word,  voyage : 1
The frequency of the word,  canceled : 1
The frequency of the word,  delay : 1
The frequency of the word,  recorded : 1
The frequency of the word,  man : 1
The frequency of the word,  craft : 1
The frequency of the word,  or : 1
The frequency of the word,  even : 1
The frequency of the word,  letter : 1
The frequency of the word,  lost : 1
The frequency of the word,  accordingly : 1
The frequency of the word,  despite : 1
The frequency of the word,  strong : 1
The frequency of the word,  competition : 1
The frequency of the word,  from : 1
The frequency of the word,  france : 1
The frequency of the word,  passengers : 1
The frequency of the word,  choose : 1
The frequency of the word,  line : 1
The frequency of the word,  preference : 1
The frequency of the word,  others : 1
The frequency of the word,  be : 2
The frequency of the word,  seen : 1
The frequency of the word,  recent : 1
The frequency of the word,  survey : 1
The frequency of the word,  official : 1
The frequency of the word,  documents : 1
The frequency of the word,  given : 1
The frequency of the word,  will : 1
The frequency of the word,  astonished : 1
The frequency of the word,  uproar : 1
The frequency of the word,  provoked : 1
The frequency of the word,  accident : 1
The frequency of the word,  involving : 1
The frequency of the word,  finest : 1
The frequency of the word,  steamers : 1

'''