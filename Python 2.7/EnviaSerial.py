import serial 

"""
#===================================================================
# Forma Numero 1
#===================================================================
Comunicacion = serial.Serial("COM1") # Se le asigna a una variable
# para luego poder escribir por el puerto usando esa variable.
# Que es este caso la Variable seria Comunicacion  
# Una vez abierto se puede escribir todo lo que uno quiera con 
# <Nombre Variable>.write(<TEXTO>) Para hacerlo mas facil y leerlo 
# de manera mas sencilla a cada Texto se le incluira al final un \n 
# para asi Escribirlo como una linea. 

Veces_Enviado = 7  # Veces enviado Corresponde a una variable que
# Representa cuantas veces se envia el Texto por serial.
# El cual se coloca en el for de abajo en el range().

for i in range(0,Veces_Enviado): # Este for se encarga de Enviar n veces Como diga la Variable <Veces_Enviado>
    Comunicacion.write("hola\n")

    
Comunicacion.write("Fin\n") # Una vez terminado el Ciclo for Se imprime "Fin\n" 
# Para asi darle Fin al ciclo while que esta en el otro Archivo.py
Comunicacion.close() #Por ultimo Cerramos el Serial
"""

"""
#===================================================================
# Forma 2 
#===================================================================
Lista = [[10,11,22,33,44,55],
         [44,43,21,65,87,66]] # Una lista llena de datos de 
                              # 6 Columnas y 2 Filas 

Comunicacion = serial.Serial("COM1") # Nuevamente Se abre el Serial.

FormatoLinea = "%d,%d,%d,%d,%d,%d\n" # Se ocupa para Formatear lo escrito 
                                      # De manera mas bonita y practica.

for i in range(len(Lista)):

    Comunicacion.write(FormatoLinea %(Lista[i][0],Lista[i][1],Lista[i][2],Lista[i][3],Lista[i][4],Lista[i][5]))
    print("Se envio", (Lista[i][0],Lista[i][1],Lista[i][2],Lista[i][3],Lista[i][4],Lista[i][5]))

Comunicacion.write("Fin\n") # Se escribe "Fin\n" para Darle fin al Bucle de lectura de Binario

Comunicacion.close() # Se cierra el Puerto serial
"""

Lista = [[10,11,22,33,44,55],
         [44,43,21,65,87,66]]

Comunicacion = open("Serial.txt", 'w') # Nuevamente Se abre el Serial.

FormatoLinea = "f:%d C:%d NOSE:%d Tu:%d LA:%d Chi:%d\n" # Se ocupa para Formatear lo escrito 
                                      # De manera mas bonita y practica.

for i in range(len(Lista)):

    Comunicacion.write(FormatoLinea %(Lista[i][0],Lista[i][1],Lista[i][2],Lista[i][3],Lista[i][4],Lista[i][5]))
    print("Se envio", (Lista[i][0],Lista[i][1],Lista[i][2],Lista[i][3],Lista[i][4],Lista[i][5]))

Comunicacion.write("Fin\n") # Se escribe "Fin\n" para Darle fin al Bucle de lectura de Binario

Comunicacion.close() # Se cierra el Puerto serial


