string = input('Enter a string : ')
print('Reverse of',string,'is',string[::-1])
if string == string[::-1]:
     print(string,'is PALINDROME !!.')
else:
     print(string,'is NOT PALINDROME !!.')
