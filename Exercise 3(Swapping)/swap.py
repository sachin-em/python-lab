# swap 2 variable without third variable
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("\n\nBefore swapping\n----------------------")
print("first number = ",a)
print("second number = ",b)

#swapping
a = a + b
b = a - b
a = a - b

# or we can use a,b=b,a
print("\n\nafter swapping\n------------------------")
print("first number = ",a)
print("second number = ",b)

