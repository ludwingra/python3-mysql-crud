import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test-python-mysql'
)

cursor = midb.cursor()

# Consulta
sql = 'INSERT INTO User(name, email, nickname, age) VALUES(%s, %s, %s, %s)'
values = ('Kevin Rivera S.','kevin.ars@gmail.com','kevincho', 7)

cursor.execute(sql, values)

midb.commit()

print(cursor.rowcount)

