# Implement a program that requires current temperature in degree fahrenheit from user 
# and prints temperature in degree celcius?

temp_F = eval (input ("Enter the temperature in degree fahrenheit"))
temp_C = (5/9)*(temp_F-32)
print(f'The temperature in degree celcius is {temp_C}')