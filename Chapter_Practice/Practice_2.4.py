#Q) write python expression to evaluate:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

#(a)'ant bat cod'?
print(s1+' '+s2+' '+s3)

#(b)'ant ant ant ant ant ant ant ant ant ant'?
print((s1 + ' ')*10)

#(c)'ant bat bat cod cod cod'
print(s1 +' '+ ((s2+' ')*2) + ' '+ ((s3+' ')*3))

#(d) 'ant bat ant bat ant bat '?
temp = s1 + ' ' + s2
print(temp*3)
# or
print((s1+' '+s2+' ')*3)