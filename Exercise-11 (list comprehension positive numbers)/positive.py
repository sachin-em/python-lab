# generate list of even numbers from an existing list using list comprehension

list1 = input('Enter a list of integers seperated by comma : ')
list1 = list1.split(',')
list1 = list(map(int, list1))

posList = [ x for x in list1 if x > 0 ]

print('Your list : ',list1)
print('List of positive numbers : ',posList)
