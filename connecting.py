import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Denzel\Downloads\Database3.accdb;')
    print("Database is connected")



except pyodbc.Error as e:
    print("Error in Connection")
