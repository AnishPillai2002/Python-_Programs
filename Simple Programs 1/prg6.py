"""Write a Python program to find the sum of even digits in a number"""

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum += digit
    num = num // 10
print("The sum of even digits is: ", sum)
