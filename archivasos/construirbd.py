import sqlite3
conexion =sqlite3.connect("ventas.db")
conexion.close()

print("***USUARIOS***")
usuarios = open("usuarios.txt", "rt", encoding="utf8")
datos_usuarios = usuarios.read()
print(datos_usuarios)

print("***CLAVES***")
claves = open("claves.txt", "rt", encoding="utf8")
datos_claves = claves.read()
print(datos_claves)

print("***PRODUCTOS***")
nombre = open("nombre.txt", "rt", encoding="utf8")
datos_nombre = nombre.read()
print(datos_nombre)

print("***CODIGO DE PRODUCTO***")
codigo = open("codigo.txt", "rt", encoding="utf8")
datos_codigo = codigo.read()
print(datos_codigo)

print("***PRECIO DE PRODUCTO***")
precio = open("precio.txt", "rt", encoding="utf8")
datos_precio = precio.read()
print(datos_precio)

conexion = sqlite3.connect("ventas.db")

cursor = conexion.cursor()
tabla_usuarios = ("""CREATE TABLE USUARIO(
                IDUSUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                USUARIO TEXT UNIQUE,
                CLAVE TEXT)""")

tabla_productos = ("""CREATE TABLE PRODUCTO(
                IDPRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE TEXT,
                CODIGO TEXT,
                PRECIO NUMBER )""")

cursor = conexion.cursor()
cursor.execute(tabla_usuarios)
cursor.execute(tabla_productos)

conexion.close()

conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
lista_usuarios = datos_usuarios.split('\n')
lista_claves = datos_claves.split('\n')
for indice,valor in enumerate(zip(lista_usuarios,lista_claves)):  
    print(valor[0],valor[1])
    cursor.execute("INSERT INTO USUARIO( USUARIO, CLAVE)VALUES('"+valor[0]+"','"+valor[1]+"')") 
conexion.commit()
conexion.close()


conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
lista_nombres = datos_nombre.split('\n')
lista_codigos = datos_codigo.split('\n')
lista_precios = datos_precio.split('\n')

for indice,valor in enumerate(zip(lista_nombres,lista_codigos,lista_precios)):  
    print(valor[0],valor[1])

    cursor.execute("INSERT INTO PRODUCTO(NOMBRE,CODIGO,PRECIO)VALUES('"+valor[0]+"','"+valor[1]+"','"+valor[2]+"')")
   
conexion.commit()
conexion.close()

