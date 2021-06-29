import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test-python-mysql'
)

cursor = midb.cursor()

# Consulta
sql = 'DELETE FROM User WHERE email = %s'
values = ('kevin.ars@gmail.com', ) # debemos dejar una coma y luego espacio luego de la coma

cursor.execute(sql, values)

midb.commit()

