# Armstrong Number
num = int(input('Enter a number : '))
power = len(str(num))
temp = num
res = 0

while temp != 0:
     res += (temp % 10) ** power
     temp = int(temp / 10)

if res == num:
     print(num,'is an Armstrong Number.')
else:
     print(num,'is NOT an Armstrong Number.')
