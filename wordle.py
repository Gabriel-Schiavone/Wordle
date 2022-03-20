# take inputs
known = input('Input known letters (example: _ta__s): ')
semi_known = input('input semi-known letters (example: r____): ')
bad = input('input wrong letters (example: x,b,o,e): ').split(',')

# open file and create word list
file = open('dict.txt', 'r')
words = file.read().splitlines()
file.close()

# apply inputs to narrow down word list
guesses = [word for word in words if len(word) == len(known)]

for x in range(len(known)):
    if known[x] != '_':
        guesses = [word for word in guesses if known[x] == word[x]]

for x in range(len(semi_known)):
    if semi_known[x] != '_':
        guesses = [word for word in guesses if semi_known[x] in word and semi_known[x] != word[x]]

for x in range(len(bad)):
    guesses = [word for word in guesses if bad[x] not in word]

# print guesses
print('\nI found these possible words:')
print(guesses)
