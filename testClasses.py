from dbConnection import dbConnection


dbConnect = dbConnection.connectDB()


dbConnection.addPlayer(dbConnect, "kevin", "abcd")


#dbConnection.getUsernames(dbConnect)
