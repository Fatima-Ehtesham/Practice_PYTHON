# Q)write type of object these expressions evaluates to:
# (a) False + False?
a = print(type(False + False))          # <class 'int'>

# (b) 2*3**2.0?
b = print(type(2*3**2.0))               # <class 'float'>

# (c) 4 // 2 + 4 % 2?
c = print(type(4 // 2 + 4 % 2))         # <class 'int'>

# (d) 2 + 3 == 4 or 5 >= 5?
d = print(type(2 + 3 == 4 or 5 >= 5))   # <class 'bool'>
