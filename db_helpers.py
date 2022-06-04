from sre_parse import State
from dbcreds import *
import mariadb

def connect_db():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(host=host,port=port,database=database,user=user,password=password)
        cursor=conn.cursor()
        return(conn, cursor)
    except mariadb.OperationalError as e: # This will allow to print the exception as it happens
        print("Got an operational error")
        if ("Access Denied" in e.msg):
            print("Failed to log in")
        disconnect_db(conn, cursor)
        
    # if (e.msg.find("Access denied") != -1)
    
def disconnect_db(conn,cursor):
    if(cursor !=None ):
        cursor.close()
    if (conn != None):
        conn.rollback()
        conn.close()

# The run_query() closes the connection once it retrieves the info so I thought if I create a login_query()
# I could bypass it but I couldn't get the authentication down.  
# I have a sneaky suspicion that having run_query() in a while loop would alleviate this,
# but I didn't explore that yet as I've been trying to formulate the credential check
# def login_query(statement):
#     try:
#         (conn,cursor) = connect_db()
#         cursor.execute(statement)
#         user = cursor.fetchall()
#         print(user)
#         return user
#     except Exception:
#         print    
        
            
    
        
    
    # for user in users:
    #     if username == user:
    #         print(user)
    #         password = input(str("Password: "))
    #         for password in users:
    #             if password == users:
    #                 print("You have successfully logged in.")
    #             else:
    #                 print("Your credentials don't match.")
    #         else:
    #             print("No username found.  Please try again:")
    #             input()
    
def run_query(statement, args=None):
    try:
        (conn, cursor) = connect_db()
        if statement.startswith("SELECT"):
            cursor.execute(statement,args)
            results = cursor.fetchall()
            print(results)
            # print("Total of {} users".format(cursor.rowcount))
            return results
            # Get the first person from the results list, then retrieve the 2nd index(column) from that row
            # print(result[0][1])
        elif statement.startswith("INSERT"):
            cursor.execute(statement,args)
            conn.commit()
            print("Welcome, you are now registered!")
        elif statement.startswith("UPDATE"):
            cursor.execute(statement,args)
            conn.commit()
            print("Your information was successfully updated!")
        else:
            cursor.execute(statement, args)
            if cursor.rowcount == 1:
                conn.commit()
                print("Query successful")
            else:
                print("Query failed")
    
    except mariadb.OperationalError as e: # This will allow to print the exception as it happens
        print("Got an operational error")
        if ("Access Denied" in e.msg):
            print("Failed to log in")
    
    # except mariadb.IntegrityError as e: # I NEED TO SET CONSTRAINTS FIRST
    #         print("Integrity error")
    #         print(e.msg)
    
    except mariadb.ProgrammingError as e:
        if("SQL syntax" in e.msg):
            print("Apparently you cannot run program")
        else:
            print("Got a different programming error")
            print(e.msg)

    except RuntimeError as e:
        print("Caught a runtime error")
        print(e.msg)

    except Exception as e:
        print(e.with_traceback)
        print(e.msg)
        # Better if solution:
        if ("Access denied" in e.msg):
            print("Failed to login")
            print(e.msg)
    finally:
        disconnect_db(conn, cursor)
        print("Database disconnected")
        
# def check_credentials(username, password):
    