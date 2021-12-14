# create a list of vowels from a given string using list comprehension

vowels = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]

string = input("Enter a string : ")
vow = [ v for v in string if v in vowels ]

print('Vowels in',string,' are', vow)
