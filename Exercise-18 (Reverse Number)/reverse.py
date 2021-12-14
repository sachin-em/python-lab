# reverse of a number
num = int(input('Enter a number : '))
rev = 0
temp = num

while temp != 0:
     rev *= 10
     rev = rev + temp % 10
     temp = int(temp / 10)
     
print('Reverse of',num,'is',rev)
     
