# Fibonacci series with n terms using functions

limit = int(input("Enter the limit : "))
prev = 0
current = 1

if limit <= 0:
     print("Please enter a limit greater than 0")
elif limit == 1:
     print("Printing fibonacci series\n---------------------------------")
     print(prev)
elif limit == 2:
     print("Printing fibonacci series\n---------------------------------")
     print(prev,',',current)
else:
     result = '' + str(prev) + ' , ' + str(current)
     for i in range(2,limit):
          nth = prev + current
          prev = current
          current = nth
          result += ' , ' + str(nth)

     print("Printing fibonacci series\n---------------------------------")
     print(result)
     
          
     
     
