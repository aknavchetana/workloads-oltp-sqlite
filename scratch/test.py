import sqlite3

#setting up the connection to the database
connection = sqlite3.connect("aquarium.db")

#total number of database rows that are impacted
print(connection.total_changes)

#getting handle to execute queries on the database
cursor = connection.cursor()

#use this to determine if the tables exist before creating them. 
listOfTables = cursor.execute(
  """SELECT tbl_name FROM sqlite_master WHERE type='table'
  AND name='fish'; """).fetchall()
 
if listOfTables == []:
    cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
    print('Table not found!')
else:
    print('Table found!')



cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()

print(rows)
target_fish_name = "Jamie"
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name = ?",
    (target_fish_name,),
).fetchall()
print(rows)