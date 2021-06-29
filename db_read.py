import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test-python-mysql'
)

cursor = midb.cursor()

cursor.execute('select * from User')

# Obtener una lista de registros
resultado = cursor.fetchall()

# # Obtener un registro
# resultado = cursor.fetchone()

print(resultado)


