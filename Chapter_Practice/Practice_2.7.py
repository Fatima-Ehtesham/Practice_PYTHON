# Q) grades = [9,7,7,10,3,9,6,6,2] , write
# (a) an expression that evaluates number of 7 grades?
grades = [9,7,7,10,3,9,6,6,2]
no_7_grades = grades.count(7)
print(no_7_grades) 

# (b) a statement that changes the last grade to 4?
# python list are mutable
grades[-1] = 4
print (grades)
# or 
# grades[8] = 4

# (c) an expression that evaluates to maximum grade?
max_grade = max(grades)
print (max_grade)

# (d) an expression that sorts the lists grade?
grades.sort()
print (grades) # in ascending order.
grades.reverse()
print(grades)  #in descending order.

# (c) an expression that evaluates to average grade?
Avg_grade = sum (grades) / len (grades)
print (Avg_grade)