# make mean of numbers
numlist = list()
while True:
    inp = input('Enter a numer: ')
    if inp =='done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)