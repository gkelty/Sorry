import mysql.connector
from mysql.connector import errorcode


class dbConnection:

    def connectDB(query):
        newQuery = query
    
        try:
            dbConnect = mysql.connector.connect(user = "gkelty_admin",
                                            password = "<newPassword1234>",
                                            host = "webdb2.uvm.edu",
                                            db = "GKELTY_Sorry!")
            query = dbConnect.cursor()

            query.execute(newQuery)

            for row in query.fetchall():
                print("Username: " + row[1])


        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
    
        else:

            dbConnect.close()



        
