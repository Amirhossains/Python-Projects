# stored_password = "1375"

# intered_password = input("pleas inter the password : ")

# if intered_password == stored_password :
#     print("your loging is successfully.")
# else :
#     print("you are wrong, try again!")

## valei hamishe while estefade mishe


# stored_password = "83624"
# intered_password = input("Pleas inter the password : ")


# while stored_password != intered_password :
#     intered_password = input("oh your password is not correct!! \ntry again : ")
# else :
#     print("your password is correct. \nhave good time:)")

## hala mighaiim alave bar password , user name ham begirim

# users = {
#     "amir rt" : "4179",
#     "ali"     : "9725",
#     "mohammad": "0286"
# }

# intered_username = input("Pleas inter your user name : ")
# intered_password = input("Pleas inter the password : ")

# if intered_username in users and intered_password == users[intered_username] :
#     print("yes you are our user.")
# else :
#     print("you are not our users!!")



users = {
    "amir rt" : "4179",
    "ali"     : "9725",
    "mohammad": "0286"
}
intered_username = input("Pleas inter your user name : ")
intered_password = input("Pleas inter the password : ")


while intered_username not in users or intered_password != users[intered_username] :
    print("Oh you wrong!!!Pleas try again.")
    intered_username = input("inter the username again : ")
    intered_password = input("inter the password again : ")
else :
    print("Yes, you are our users. \nhave good time :)")