#Practice_3.11:
# Implement a function that takes a list of integers and returns True if all integers in list are even, otherwise False?
lst = []
for integers in range(4):
    lst_input = eval(input("Enter a integer: "))
    lst.append(lst_input)
print(lst)

def all_even(lists):
    count = 0
    for numbers in range(len(lists)):
        if(lists[numbers] % 2 == 0):
            count += 1 
    if(count == len(lists)):
        print("All elements of list are even")
        return True
    else:
        print("All elements of list are not even")
        return False

res = all_even(lst)
print(res)