# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:41:50 2020

@author: osito
"""


import sqlite3
conexion =sqlite3.connect("ventas.db")

usuario = input("USUARIO: ")
clave = input("CLAVE: ")

cursor=conexion.cursor()
cursor.execute("SELECT Usuario from USUARIO where USUARIO= '" + usuario+"' AND clave='"+clave+"'")
listaUsuario= cursor.fetchall()
print(listaUsuario)

if("'"+usuario+"'" == listaUsuario):
    print("errorrrrrr")
    
else:
    print("yes")
    
