"""Write a program to read P,T, R and calculate simple interest.(SI=(P*T*R)/100)"""

p=float(input("Enter the principal amount: "))
t=float(input("Enter the time period: "))
r=float(input("Enter the rate of interest: "))

si=(p*t*r)/100
print("The simple interest is: ",si)