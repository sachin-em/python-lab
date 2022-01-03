size = int(input("Enter step size : "))

def printPyramid(n):
     s = ''
     for i in range(1, n+1):
          s += '\n'
          for j in range(1, i+1):
                 temp = i * j
                 s += ' ' + str(temp)

     print(s)

printPyramid(size)
          
