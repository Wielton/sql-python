from db_helpers import *


# This is the main objective complete:

# user = input(str("Please enter your name: "))
# todo = input(str("Hello {} please select 1 to post, or 2 to see all posts: ".format(user)))

# if todo == "1":
#     post = input(str("Begin: "))
#     run_query("INSERT INTO blog_post(username,content) VALUES (?,?)", [user,post])
    
# elif todo == "2":
#     run_query("SELECT * FROM blog_post")

# ------------------------------------------------------------------------------------------------------




# THIS WILL ALLOW TO SIGN UP OR LOGIN.  I have a user signup somewhat complete. 
# I am trying to get login credentials passed, have tried many different things.  I feel I'm close...

selection = input("Welcome to Blog! Please choose an option: 1. Signup or 2. Login. Type exit at any time to leave.")
# I didn't try anything within the while loop
# while True:  

# I did not create an instance of a user but I feel like I need to so I began to build one in db_helpers
if selection == "1":
    user_email = input(str("Email: "))
    user_username = input(str("Username: "))
    user_password = input(str("Password: "))
    user_first_name = input(str("First Name: "))
    user_last_name = input(str("Last Name: "))
    run_query("INSERT INTO users(username,email,first_name,last_name,password) VALUES (?,?,?,?,?)", [user_username,user_email,user_first_name,user_last_name,user_password])

# ----------------------------------------------------------------------------------------------------------
# I couldn't get this working:
# if selection == "2":
#     input_name = input("Username: ")
#     users = login_query("SELECT * FROM users")
#     for i in users:
#         if (input_name != users[i].username):
#             print("Username doesn't exist")
#     else:
#         print("Username accepted")
#         input_password = input("Password: ")
#         password = login_query("SELECT password FROM users WHERE username=?", input_name)
#         if (input_password != password):
#             print("Credentials don't match")
#         else:
#             print("Password accepted")
# else:
#     print("Credentials failed")
    

    
