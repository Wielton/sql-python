import dbcreds
import mariadb

#connect to mariadb
conn = mariadb.connect(
                        user=dbcreds.user,
                        password=dbcreds.password,
                        host=dbcreds.host,
                        port=dbcreds.port,
                        database=dbcreds.database,
                        )
# now use the db to create a cursor object.  a cursor is a function to 
user = input("Please enter your username: ")
print("You have two options:")
print("1. Write a new post")
print("2. See all other posts")
selection = input("Choose 1 or 2: ")

if selection == "1":
    content = input("Write your post:")
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
#once your commit is complete, close the connection and treat it like an opening and closing block of code
    cursor.close()
    conn.close()