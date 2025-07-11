import mysql.connector as connector

mydb = connector.connect(
    host="localhost",
    user="root",
    password="1234",
    port=3306
)

print('Connected to MySQL Server',mydb)

cursor = mydb.cursor()

# Show all databases
# print("Databases in MySQL Server:")
# result = cursor.execute("SHOW DATABASES")
# result = cursor.fetchall()
# for db in result:
#     print(db)

# Create a new database
# query = "CREATE DATABASE IF NOT EXISTS user_management"
# cursor.execute(query)
# mydb.commit()
# print("Database created successfully")

# Create a new table
query = "USE user_management"
cursor.execute(query)

# query = """CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL UNIQUE)"""
# cursor.execute(query)
# mydb.commit()
# print("Table created successfully")

# Insert data into the table
# query = """INSERT INTO users (id, name, email) VALUES 
#         (1, "Meharsh", "meharsh7804@gmail.com"),
#         (2, "Aman", "patne@gmail.com"),
#         (3, "Nikunj", "chhatani@gmail.com")"""
# cursor.execute(query)
# mydb.commit()
# print("Data inserted successfully")

# Update data in the table
# query = """UPDATE users SET email = "chandure@gmail.com" WHERE id = 1"""
# cursor.execute(query)
# mydb.commit()
# print("Data updated successfully")

# Delete data from the table
query = """DELETE FROM users WHERE id = 1"""
cursor.execute(query)
mydb.commit()
print("Data deleted successfully")
query = "SELECT * FROM users"
cursor.execute(query)
result = cursor.fetchall()
print("Data in the table:")
for row in result:
    print(row)
