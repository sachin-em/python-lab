# swap first char of 2 strings and create one string seperated by space

strings = input("Enter two strings seperated by space : ")
strList = strings.split(' ')

string = ''
string = string + strList[1][0] + strList[0][1:] + ' ' + strList[0][0] + strList[1][1:]

print('String after swapping first character : ',string)

