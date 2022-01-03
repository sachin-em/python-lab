# find factorial of a number using function

num = int(input("Enter a number : "))
def fact(n):
     if n <= 1:
          return 1
     else:
          f = n * fact(n-1)
          return f

print("Factorial of",num,"is",fact(num))
     
