#write python boolean expressions of following and evaluate them:
# (a)sum of 2 and 2 is less than 4?
chk_sum = 2 + 2
ans = chk_sum < 4
print(ans)

# (b)value of 7//3 is equal to 1+1?
a= 7//3 == 1+1
print(a)
#or
#(7//3) == (1+1)

#(c) sum of 3 squared and 4 squared is equal to 25?
b=((3**2)+(4**2) == 25)
print(b)

# (d)The sum of 2,4 and 6 is greater than 12?
print(2+4+6 > 12)

# (e)1387 is divisible by 19?
print(1387%19 == 0)
# (f)31 is even?
print(31%2 == 0 and True)
#or
print(31%2 == 0)
# or
print((((31%2) == 0) and True))

# (g)The lowest price among $34.99, $29.95, $ 31.50 is less than $30.00?
print(min(34.99,29.95,31.50) < 30.00)