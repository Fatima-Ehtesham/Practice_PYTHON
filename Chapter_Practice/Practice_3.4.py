# Q) Implement a program that starts by asking user to enter login id (string), then it checks 
# whether id is in list ['joe','sue','hani','sophie'] of valid users?

login_id = input("Enter your ID: ")
valid_user_id = ['joe','sue','hani','sophie']
if login_id in valid_user_id :
    print("valid user")
    print("You are in!")
else:
    print("Invalid user")
print("Done")