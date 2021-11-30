def readDict(num):
	n = int(input("Enter num of values to insert to dictionary {}: ".format(num)))
	d={}
	for i in range (n):
		key = input('Enter key : ')
		val = input('Enter value for {} : '.format(key))
		d[key] = val
	return d
	
d1 = readDict(1)
d2 = readDict(2)

print('Before merge\n',d1,'\n',d2)
d1.update(d2)
print('After merging \n ',d1)
