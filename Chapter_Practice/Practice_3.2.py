# Translate conditional statements into python if statement:
# (a)If age is greater than 62, print, 'You can get your pension benefits'?
age = eval(input ("enter your age"))
if (age > 62):
    print('You can get your pension benefits')
print("Thank you")
# (b) If name is in list ['Musial','Aaraon','Williams','Gehrig','Ruth'], print, "one of top five baseball players ever"?
baseball_player_list = ['Musial','Aaraon','Williams','Gehrig','Ruth']
name = input ("enter name of a baseball player")
if (name in baseball_player_list):
    print ("one of top five baseball players ever")
# (c) If atleast one of Boolean variables north, south, east, west is true, 
# print, "I can escape"?
north = False 
south = True
east = False
west = False
if (north or south or east or west):
    print("I can escape") 