import pyodbc
try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Denzel\Downloads\Database3.accdb;')
    print("Database is connected")

    record = connection.cursor()
    record.execute('SELECT * from Table1')
    for row in record.fetchall():
        print(row)


except pyodbc.Error as e:
    print("Error in Connection")

