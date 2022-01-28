#Add appropriate docstring to following function?

lst = []
for integers in range(4):
    lst_input = eval(input("Enter a integer: "))
    lst.append(lst_input)
print(lst)

def print_negative_values(lists):
    'This function gives negative values of a list as output'
    print("negative values of list are: ")
    for values in lists:
        if (values < 0):
            print(values)  
print_negative_values(lst)

no_1 = eval(input("Enter a number"))
no_2 = eval(input("Enter another number"))

def average(a, b):
    "This function returns average of two numbers"
    sum_no = a+b 
    avg_no = sum_no / 2 
    return avg_no
    
res = average(no_1, no_2)
print(f'average of given numbers is {res}')

help(print_negative_values)
help(average)