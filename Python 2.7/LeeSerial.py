import serial 


Comunicacion = serial.Serial("COM2") # Se abre Puerto serial
Lista = []
while True:
    Recibido = Comunicacion.readline()
    Recibido = str(Recibido)
    Recibido = Recibido[:-1]
    Lista.append(Recibido)
    
    
    if Recibido == 'Fin\n':
        break

    print(Recibido)

Comunicacion.close()

print(Lista)
