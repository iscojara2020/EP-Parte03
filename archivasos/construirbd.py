import sqlite3
conexion =sqlite3.connect("VENTAS.db")

tabla_usuario = """ CREATE TABLE USUARIO(
                    IDUSUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                    USUARIO TEXT UNIQUE,
                    CLAVE TEXT
                )                
                """

tabla_producto = """ CREATE TABLE PRODUCTO(
                    IDPRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    CODIGO TEXT,
                    PRECIO NUMBER
                )                
                """
print("***USUARIOS***")
usuarios = open("usuarios.txt","rt", encoding='utf8')
datos_usuarios = usuarios.read()
print(datos_usuarios)

print("***CODIGOS***")
codigo = open("codigo.txt","rt", encoding='utf8')
datos_codigo = codigo.read()
print(datos_codigo)

print("***CLAVES***")
claves= open("claves.txt","rt", encoding='utf8')
datos_claves = claves.read()
print(datos_claves)

print("***PRODUCTOS***")
nombre = open("nombre.txt","rt", encoding='utf8')
datos_nombre = nombre.read()
print(datos_nombre)

print("***PRECIOS***")
precio = open("precio.txt","rt", encoding='utf8')
datos_precio = precio.read()
print(datos_precio)

cursor = conexion.cursor()
lista_usuario = [('Patrick','000'),
                 ('Diana','111'), 
                 ('Francisco','222'),
                 ('Luis','333'),  
                 ('Ana','444') 
                ]

lista_producto=[('azucar','0001','3.5'),
                   ('harina','0002', '6.5'),
                   ('fideo','0003', '2.8'),
                   ('arroz','0004', '3.0'),
                   ('leche','0005', '3.5'),
                   ('yogurt','0006', '5.5'),
                   ('paneton','0007', '15.0'),
                   ('chocolate','0008', '2.0'),
                   ('ricocan','0009', '6.0'),
                   ('atun','0010', '4.5')
                   ]

consulta_usuario = """ INSERT INTO USUARIO (USUARIO, CLAVE)
                    VALUES(?,?)
                """
consulta_producto = """ INSERT INTO PRODUCTO (NOMBRE, CODIGO, PRECIO)
                         VALUES(?,?,?)
                    """

cursor = conexion.cursor()
cursor.execute(tabla_usuario)
cursor.execute(tabla_producto)

cursor.executemany(consulta_usuario, lista_usuario)
cursor.executemany(consulta_producto, lista_producto)

conexion.commit()
conexion.close()

