#Practice_3.9:
# Implement a function that takes two numbers as input and returns average of numbers?
no_1 = eval(input("Enter a number: "))
no_2 = eval(input("Enter another number: "))
def average(a, b):
    sum_no = a+b 
    avg_no = sum_no / 2 
    return avg_no
res = average(no_1, no_2)
print(f'average of given numbers is {res}')