# Q) Implement a program that takes from user a list of words, and prints on 
# screen all four letter words from list?

lists = []
for elements in range(4):
    user_input = input("Enter a string: ")
    lists.append(user_input)
print(f'data entered is {lists}')
print ("Four letter input strings are: ")
for list_elements in lists:
    if len(list_elements)==4 :
        print(list_elements)
print("Done Executing...")