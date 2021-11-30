# print colors in colorList1 that is not contained in colorList2

colorList1 = input('Enter  a list of colors seperated by comma : ')
colorList2 = input('Enter  another list of colors seperated by comma : ')

colorList1 = colorList1.split(',')
colorList2 = colorList2.split(',')

set1 = set(colorList1)
set2 = set(colorList2)

if len(set1-set2) > 0:
     print('Colors that are present in List 1 and Not present in List 2\n------------------------------------------------------------------')
     print(set1-set2)
else:
     print('Colors in List 1 is also present in list 2')

