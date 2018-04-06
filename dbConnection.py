import mysql.connector
from mysql.connector import errorcode

# This class will be used to make all of the SQL commands we will need. 
class dbConnection:

# This method sets up the connection to the DB. Should be called before performing any query
    def connectDB():

        try:
            dbConnect = mysql.connector.connect(user = "gkelty_admin", password = "<newPassword1234>",
                                                host = "webdb2.uvm.edu",  db = "GKELTY_Sorry!")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


        return dbConnect
    
    # This method is called when a user signs up. It will add a player to our DB. 
    def addPlayer(dbConnect, username, password):
        
        newQuery = ("INSERT INTO tblPlayer (playerID, username, userPassword) VALUES (null," + "'" + username+ "'" + "," + "'" + password + "'" + ")")
        print(newQuery)

        query = dbConnect.cursor()

        query.execute(newQuery)
        dbConnect.commit()

        print("Qeury was executed!")
