#Practice_3.16:
# Implement a function that takes a list of integers as input and prints values of list 
# after swapping 1st and last element of list? The function doesnot return anything. 

lst = []
for integers in range(4):
    lst_input = eval(input("Enter a integer: "))
    lst.append(lst_input)
print(f'original list is {lst}')

def swap_fn(list):
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
    print(f'After swapping first and last value, list is {list}')
    
swap_fn(lst)