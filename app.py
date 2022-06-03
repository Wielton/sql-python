from db_helpers import *

user = input(str("Please enter your name: "))
todo = input(str("Hello {} please select 1 to post, or 2 to see all posts: "))

if todo == "1":
    post = input(str("Begin: "))
    run_query("INSERT INTO blog_post(username,content) VALUES (?,?)", [user,post])
    
elif todo == "2":
    run_query("SELECT * FROM blog_post")


# THIS WILL ALLOW TO SIGN UP OR LOGIN
# selection = input("Welcome to Blog! Please choose an option: 1. Signup or 2. Login ")

# if selection == "1":
#     user_email = input(str("Email: "))
#     user_username = input(str("Username: "))
#     user_password = input(str("Password: "))
#     user_first_name = input(str("First Name: "))
#     user_last_name = input(str("Last Name: "))
#     run_query("INSERT INTO users(username,email,first_name,last_name,password) VALUES (?,?,?,?,?)", [user_username,user_email,user_first_name,user_last_name,user_password])
    
# elif selection == "2":
#     user_username = input(str("Username: "))
#     user_password = input(str("Password: "))
#     run_query("SELECT username FROM users ")
# else:
#     print("Retry")
#     input()
    
    

    
