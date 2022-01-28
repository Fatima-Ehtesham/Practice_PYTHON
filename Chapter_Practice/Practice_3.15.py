#Practice_3.15:
# Implement a program that takes a list of integers as input and prints 
# values of list after swapping 1st and last element of list? 

lst = []
for integers in range(4):
    lst_input = eval(input("Enter a integer: "))
    lst.append(lst_input)
print(f'original list is {lst}')

temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
print(f'After swapping first and last value, list is {lst}')