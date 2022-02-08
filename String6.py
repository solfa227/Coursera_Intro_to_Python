data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)  #finds the first space positin after @ position
print(sppos)

host = data[atpos+1 : sppos]
print(host)

first_sspos = data.find(' ')
print(first_sspos)
second_sspos = data.find(' ',first_sspos+1)
print(second_sspos)
name = data[first_sspos+1 : second_sspos]
print(name)