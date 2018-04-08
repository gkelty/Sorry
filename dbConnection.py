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

#This method grabs the usernames in our DB at the time of call and puts them in an array and returns. 
    def getUsernames(dbConnect):
        
        query = dbConnect.cursor()

        query.execute("SELECT username FROM tblPlayer;")

        usernames = query.fetchall()

        usernameArray = []
        for username in usernames:
            username = str(username)
            usernameArray.append(username.strip("')(,"))
            
        return usernameArray
    
    # This method is called when a user signs up. It will add a player to our DB. 
    def addPlayer(dbConnect, newUser, password):
        
        query = dbConnect.cursor()

        usernames = dbConnection.getUsernames(dbConnect)


        if newUser not in usernames:
            newQuery = ("INSERT INTO tblPlayer (playerID, username, userPassword) VALUES (null," + "'" + newUser+ "'" + "," + "'" + password + "'" + ")")
            query.execute(newQuery)
            dbConnect.commit()
            print("Qeury was executed!")
        else:
            print("Username is already taken!")




            

        

        
