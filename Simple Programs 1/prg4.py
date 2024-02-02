"""Find the biggest and smallest of three numbers.( use min and max function)"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
biggest = max(a, b, c)
smallest = min(a, b, c)
print("The biggest number is: ", biggest)
print("The smallest number is: ", smallest)