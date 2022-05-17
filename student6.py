import pyodbc
try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Denzel\Downloads\Database3.accdb;')
    print("Database is connected")

    user_id = 6
    Contact = "911"
    Address = "Quiapo"
    Fullname = "Denzel Rafael K. Donato"
    Birthdate = "07/20/2003"
    Sem = 100
    record = connection.cursor()
    record.execute('update Table1 SET Address=? WHERE id=?',(Address, user_id))
    record.execute('update Table1 SET Sem=? WHERE id=?',(Sem, user_id))
    record.execute('update Table1 SET Fullname=? WHERE id=?',(Fullname,user_id))
    record.execute('update Table1 SET Birthdate=? WHERE id=?', (Birthdate, user_id))
    record.execute('update Table1 SET Contact=? WHERE id=?', (Contact, user_id))
    record.commit()
    print("Database is updated")


except pyodbc.Error as e:
    print("Error in Connection")