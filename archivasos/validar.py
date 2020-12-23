# -*- coding: utf-8 -*-

import sqlite3
conexion =sqlite3.connect("ventas.db")
#listar producto
def listar():
    conexion = sqlite3.connect("ventas.db")
    cursor=conexion.cursor()
    cursor.execute("""Select * from Producto
                   """)
    personas=cursor.fetchall()
    #encabezado de tabla
    print('{:^50}{:^50}{:^50}'.format('Nombre','Codigo','Precio'))
    print("---------------------------------------------------------------------------")
    for persona in personas:
        print('{:^50}{:^50}{:^50}'.format(persona[1],persona[2],persona[3]))
#ingresar produto
def ingresar():
    conexion = sqlite3.connect("ventas.db")
    cursor=conexion.cursor()
    nombreProducto = input("Ingrese nombre del producto: ")
    CodigoProducto = input("Ingrese codigo del producto: ")
    PrecioProducto = (input("Ingrese precio del producto: "))
    
    cadena="INSERT INTO Producto(NOMBRE,CODIGO,PRECIO) VALUES('"+nombreProducto+"','"+CodigoProducto+"','"+PrecioProducto+"')"
    cursor.execute(cadena)
        
    conexion.commit()
    print("\nProducto Ingresado..........")
# Modificar producto
def modificar():    
    cursor = conexion.cursor()
    CodigoProducto = input("Ingrese codigo del producto a modificar: ")
    nombreProducto = input("Ingrese nuevo nombre: ")
    PrecioProducto = (input("Ingrese nuevo precio: "))
    consulta ="UPDATE Producto SET nombre ='"+nombreProducto+"' ,precio='"+PrecioProducto+"' WHERE CODIGO='"+CodigoProducto+"'"
    cursor = conexion.cursor()
    cursor.execute(consulta)
    
    conexion.commit()
    print("\nProducto modificado..........")
def eliminar():    
    cursor = conexion.cursor()
    CodigoProducto = input("Ingrese codigo del producto a eliminar: ")
    consulta ="DELETE FROM Producto WHERE CODIGO='"+CodigoProducto+"'"
    cursor = conexion.cursor()
    cursor.execute(consulta)
    
    conexion.commit()
    print("\nProducto eliminado..........")   
#pedir datos usuario
usuario = input("USUARIO: ")
clave = input("CLAVE: ")

cursor=conexion.cursor()
cursor.execute("SELECT * from USUARIO where USUARIO= '" + usuario+"' AND clave='"+clave+"'")
listaUsuario= cursor.fetchall()
tamaño=len(listaUsuario)

    #validacion
if tamaño != 0:
    for persona in listaUsuario:
        if(usuario==persona[1]  and clave==persona[2]):
            print("\nBienvenido al sistema")
            def pedirNumeroEntero():
                correcto=False
                num=0
                while(not correcto):
                    try:
                        num = int(input("Introduce un numero entero: "))
                        correcto=True
                    except ValueError:
                        print('Error, introduce un numero entero')
     
                return num
 
            salir = False
            opcion = 0
 
            while not salir:
                print("--------------------------------------------")
                print("\tDatos Producto")
                print ("\n1. Listar")
                print ("2. Agregar")
                print ("3. Eliminar")
                print ("4. Modificar")
                print ("5. Salir")
                 
                print ("\nElige una opcion")
                print("--------------------------------------------")
             
                opcion = pedirNumeroEntero()
             
                if opcion == 1:
                    print("\nLista de Productos")
                    listar()
                elif opcion == 2:
                    ingresar()
                elif opcion == 3:
                    eliminar()
                elif opcion == 4:
                    modificar()
                elif opcion == 5:
                    salir = True
                else:
                    print ("Introduce un numero entre 1 y 4")
             
            print ("Fin del menu Prducto :)")
else:
     print("Error, datos no validos")
