# counting words in a file
fname = input('Enter the file name: ')
fhand = open(fname)
inp = fhand.read()
for line in inp:
    words = inp.split() 
print('Counting...')
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1 
for key in counts:
    print(key, counts[key])

# Retrieving Lists of Keys and Values
print('List: ', list(counts))
print('Keys: ', counts.keys())
print('Values: ', counts.values())
print('Items:', counts.items())

# Two Iteration Variables
for m,n in counts.items():
    print(m,n)
    
# find the bigest word count
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print('The largest count word is: ', bigword, bigcount)