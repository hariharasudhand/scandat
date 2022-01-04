from PyQt5.QtSql import QSqlDatabase

con = QSqlDatabase.database("con1", open=False)

con.databaseName()

con.connectionName()