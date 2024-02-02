"""write a program to convert temperature in degree Fahrenheit to Celsius."""


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print("Temperature in Celsius is: ", temp_celsius)