# read list of integers and replace integers greater than 100 with over

ints = input("Enter a list of integers seperated by space : ")
intList = ints.split(" ")

index = 0
for integer in intList:     
     if int(integer) > 100:
          intList[index] = "Over"
          
     index += 1

print(intList)
