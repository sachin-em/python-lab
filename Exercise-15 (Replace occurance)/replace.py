# replace occurance of first character with $ except first char
string = input('Enter a string : ')
strList = list(string)

firstChar = strList[0]
for index, s in enumerate(strList):
     if s == firstChar and index != 0:
          strList[index] = '$'

newStr = ''
for i in strList:
     newStr += i
print('String you entered : ',string)
print('Modified string : ',newStr)
