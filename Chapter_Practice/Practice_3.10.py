#Implement a function that takes a string as input and returns true if no character in string is a 
# vowel, otherwise false?

user_input = input("Enter a string: ")

def no_vowel(string_input):
    vowel = str()
    flags = False
    for chars in string_input:
        if chars in 'aeiouAEIOU':
            vowel += chars
            flags = True
    if (flags == False):
        print("no vowel")
        return True
    else:
        print('vowels in string are ')
        print (vowel)
        return False
        
print(no_vowel(user_input))