import mysql.connector
from mysql.connector import OperationalError

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="bincom_test"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS bincom_test")

mydb.commit()


def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sql_commands = sql_file.split(';')

    # Execute every command from the input file
    for command in sql_commands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            mycursor.execute(command)
            mydb.commit()
        except OperationalError as msg:
            print("Command skipped: ", msg)


mycursor.execute(executeScriptsFromFile('schema.sql'))
