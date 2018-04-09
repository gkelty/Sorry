from dbConnection import dbConnection


dbConnect = dbConnection.connectDB()


dbConnection.addPlayer(dbConnect, "bbbb", "abcd")


#dbConnection.getUsernames(dbConnect)
