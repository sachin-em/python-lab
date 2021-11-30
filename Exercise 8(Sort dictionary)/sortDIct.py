# sort dictionary in ascending and descending order

n = int(input("Enter num of values to insert : "))
d={}
for i in range (n):
	key = input('Enter key : ')
	val = input('Enter value for {} : '.format(key))
	d[key] = val
	
print('\nBefore sorting : ', d)
print('\nAfter sorting (Ascending order) : ', sorted(d.items()))
print('\nAfter sorting (Descendng order) : ', sorted(d.items(), reverse = True))
	


