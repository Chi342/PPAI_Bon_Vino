import pyodbc

#Connection information
# Your SQL Server instance
sqlServerName = '.'
#Your database
databaseName = 'Bon_vino'
# Use Windows authentication
trusted_connection = 'yes'
# Connection string information
connenction_string = (
f"DRIVER={{SQL Server}};"
f"SERVER={sqlServerName};"
f"DATABASE={databaseName};"
f"Trusted_Connection={trusted_connection}"
)
try:
   # Create a connection
   connection = pyodbc.connect(connenction_string)
   cursor = connection.cursor()
   # Run the query to the Person.Person table
   query = 'SELECT * FROM Vino'
   cursor.execute(query)
   # print the results of the row
   rows = cursor.fetchall()
   for row in rows:
      print(row)
except pyodbc.Error as ex:
      print("An error occurred in SQL Server:", ex)
# Close the connection
finally:
   if 'connection' in locals() and connection is not None:
       connection.close()

def listar():
    