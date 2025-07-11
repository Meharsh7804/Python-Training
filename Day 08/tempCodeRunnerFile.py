import mysql.connector as connector

mydb = connector.connect(
    host="localhost",
    user="root",
    password="123",
    port=3306
)

print('Connected to MySQL Server',mydb)

cursor = mydb.cursor()
result = cursor.execute("SHOW DATABASES")
result = cursor.fetchall()
for db in result:
    print(db)