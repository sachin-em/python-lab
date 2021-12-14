# to print extension from file name

filename = input("Enter the file name with extension : ")
ext = filename.split('.')
print('You have entered file with extesion "{}"'.format(ext[-1]))

