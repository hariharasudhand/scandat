#string functions
name = 'harish'
print(name + ' is a Rpa Devolper ')

#this is used for lower case
print(name.lower())

# this is used for upper case
print(name.upper())

#this is used for upper or lower(true or flase)
print(name.isupper())
print(name.islower())

#find the length of the string
print(len(name))

#find the index of string
print(name[0:3])
print(name.index('r'))
print(name.index('har'))

#this is for replace of string
print(name.replace('harish', 'karthi'))