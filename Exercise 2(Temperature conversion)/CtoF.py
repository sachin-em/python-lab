# C to F calculator
choice = 0
while choice != 3:
     
     choice = int(input("\n\nEnter ur choice \n1.C to F\n2.F to C \n3.exit\nYour choice : "))

     if choice == 1 :
          c = input("Enter temp in degree celsius : ")
          c = int(c)
          f = (c * (9/5)) + 32
          print(c," C = ",f," F ")
     elif choice == 2 :
          f = input("Enter temp in farenheit : ")
          f = int(f)
          c = (f - 32) * (5/9)
          print(f," F = ",c," C ")
     elif choice == 3 :
          pass
     else :
          print("Enter a valid choice ")
          
          
