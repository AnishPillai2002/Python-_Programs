"""Write a Python program to print all prime numbers less than 100."""

for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")