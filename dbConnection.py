import mysql.connector
from mysql.connector import errorcode
import pygame

# text sizes
smallText = pygame.font.Font('freesansbold.ttf', 20)

# width and height of screen display
displayWidth = 600
displayHeight = 600


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

# Grabs stats from DB based on username passed to it and returns array of statistics 
    def getStats(dbConnect,username):
        query = dbConnect.cursor()
        gamesPlayed = "SELECT gamesPlayed from tblStats WHERE username = '" + username + "';"
        gamesInProgress = "SELECT gamesInProgress from tblStats WHERE username = '" + username + "';"
        totalWins = "SELECT totalWins from tblStats WHERE username = '" + username + "';"
        totalLosses = "SELECT totalLosses from tblStats WHERE username = '" + username + "';"
        totalKOs = "SELECT totalKOs from tblStats WHERE username = '" + username + "';"

        queries = [gamesPlayed,gamesInProgress,totalWins, totalLosses, totalKOs  ]

        stats = []
        
        for q in queries:
            query.execute(q)
            result = query.fetchall()
            result = str(result)
            stats.append(result.strip("'[](),"))
            
        return stats

    def incrementGamesPlayed(dbConnect,username):
        query = dbConnect.cursor()
        selectQuery = ("SELECT gamesPlayed FROM tblStats WHERE username = " + "'" + username +"'" + ";")
        query.execute(selectQuery)
        gamesPlayed = query.fetchall()
        gamesPlayed = str(gamesPlayed).strip("'[](),")
        gamesPlayed = int(gamesPlayed) + 1
        gamesPlayed = str(gamesPlayed)
        incrementQuery = ("UPDATE tblStats SET gamesPlayed = "+ "'" + gamesPlayed + "'" + " WHERE username =" + "'" + username + "'" + ";")
        print(incrementQuery)
        query.execute(incrementQuery)
        dbConnect.commit()

        
    def createStatRecord(dbConnect, username):
        query = dbConnect.cursor()
        insertQuery = ("INSERT INTO tblStats (username, gamesPlayed, gamesInProgress, totalWins, totalLosses, totalKOs) VALUES (" "'" + username + "', '0', '0', '0', '0', '0');")
        query.execute(insertQuery)
        dbConnect.commit()      
        
    # This method is called when a user signs up. It will add a player to our DB. 
    def addPlayer(dbConnect, newUser):
        import mainMenu
        query = dbConnect.cursor()
        insertQuery = ("INSERT INTO tblPlayer (playerID, username, userPassword) VALUES (null," + "'" + newUser + "'" + "," + "'" + "null" + "'" + ")")
        query.execute(insertQuery)
        dbConnect.commit()
        dbConnection.createStatRecord(dbConnect,newUser)
        mainMenu.startPage(newUser)
        

    def playerExist(username):
        dbConnect = dbConnection.connectDB()
        usernames = dbConnection.getUsernames(dbConnect)
        if username not in usernames:
            return False
        else:
            return True


# gets called when user hits button on signInDisplay() and either brings them back or
# pushes the new (unique) username to our DB
    def signIn(username, screen):
        import mainMenu
        username = username.getText()
        playerExist = dbConnection.playerExist(username)
        if  playerExist == False:
##            dbConnection.addPlayer(dbConnection.connectDB(),username)
            isNewUser = True
            mainMenu.intro(isNewUser, username)
            print("username added to DB")
            mainMenu.startPage(username)
        elif username == "":
            print("Username is empty")
            mainMenu.intro()

        else:
            mainMenu.startPage(username)
            print("Go to 'Welcome Player' page")
                
        

    
            

        


        
