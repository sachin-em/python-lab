# program to take 2 lists and check whether it is of same length, find common elements, whether the sums are equal

list1 = input("Enter a list of integers seperated by comma : ")
list1 = list1.split(",")
list1 = list(map(int,list1))
list2 = input("Enter another list of integers seperated by comma : ")
list2 = list2.split(",")
list2 = list(map(int,list2))

if len(list1) == len(list2):
     print('\nBoth lists are of same length ',len(list1))
else:
     print('\nDifferent list length.\n----------------------')
     print('Length of list 1 = ',len(list1))
     print('Length of list 2 = ',len(list2))
     
if sum(list1) == sum(list2):
     print('\n\nBoth lists sums to same value',sum(list1))
else:
     print('\nDifferent list sums\n------------------------')
     print('Sum of list 1 = ',sum(list1))
     print('Sum of list 2 = ',sum(list2))



set1 = set(list1)
set2 = set(list2)
if len(set1.intersection(set2)) > 0:
           print('\nCommon elements = ',set1.intersection(set2))
else:
           print('\nlist1 and list2 has no common elements\n')

