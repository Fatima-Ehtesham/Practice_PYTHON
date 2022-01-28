# Implement a function that takes a list of integers as input and prints negative values of list. 
#The function should not return anything?

lst = []
for integers in range(4):
    lst_input = eval(input("Enter a integer: "))
    lst.append(lst_input)
print(lst)

def print_negative_values(lists):
    print("negative values of list are: ")
    for values in lists:
        if (values < 0):
            print(values)
    
print_negative_values(lst)