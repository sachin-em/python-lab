#Read a list of integers and remove even numbers

integers = input("Enter a list of integers seperated by comma : ")

integers = integers.split(',')

for num in integers:
     if int(num) % 2 == 0:
          integers.remove(num)

print('After removing even numbers',integers)
