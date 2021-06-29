import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test-python-mysql'
)

cursor = midb.cursor()

# Consulta Actualizar datos
sql = 'UPDATE User SET nickname = %s WHERE email = %s'
values = ('kevin.ars', 'kevin.ars@gmail.com')

cursor.execute(sql, values)

midb.commit()


