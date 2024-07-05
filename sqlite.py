import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Shankar','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Suraj','Testing','B',100)''')
cursor.execute('''Insert Into STUDENT values('Ankita','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vaibhav','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Roopali','GenAi','A',35)''')

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()