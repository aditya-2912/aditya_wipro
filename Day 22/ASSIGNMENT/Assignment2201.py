import mysql.connector

host="localhost"
user="root"
password="Olympus@29"
database="wipro_db"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("connected to the database successfully")

# -------- FETCH ----------
print("\nEmployees with salary > 50000:\n")

query1 = "SELECT * FROM employee WHERE salary > 50000"
cursor.execute(query1)

result = cursor.fetchall()
for row in result:
    print(row)

# -------- INSERT ----------
print("\nInserting new employee...\n")

insert_query = """
INSERT INTO employee (idEmployee, emp_name, salary)
VALUES (%s, %s, %s)
"""

values = (6, "somu", 65000)

cursor.execute(insert_query, values)
conn.commit()
print("New employee inserted successfully")

# -------- UPDATE ----------
print("\nUpdating salary by 10%...\n")

update_query = """
UPDATE employee
SET salary = salary + salary*0.10
WHERE idEmployee = %s
"""

cursor.execute(update_query,(5,))
conn.commit()
print("Salary updated successfully")

cursor.close()
conn.close()
