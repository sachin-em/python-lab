#word count in a string

string = input("Enter a string : ")

strList = string.split(" ")
strSet = set(strList)

for word in strSet:
     count = strList.count(word)
     print(word," x ",count)
