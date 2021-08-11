import sys
k = 0
 
try:
    buff = '' #Se inicializa variables
    while True:
        buff += sys.stdin.read(1) #Se anexa la cadena recivida del sensor
        if buff.endswith('\n'): #Se ejecuta cada salto de linea
            #print( buff[:-1])  #Se puede ver lo que llega al script
            po = buff.split(" ")    #Se genera una separacion de cada parte del codigo por cada espacio
            if po[0] == 'Characteristic':   #Se utiliza esta carracteristica para no dar valides ala primera linea, que es solo cadena de strings sin datos
                print("Data Polar h7")       #Nos indica qeu se da inicio y ya llego la primera linea
            else:
                hr=int(po[6],16)            #Se extrae el valor de la frecuencia cardiaca de la cadena string y se genera la conversion de hex a dec
                print("  {} PRbpm".format(hr))  #Se escribe en cosola el valor de esta convercion 
                  #Se genera un nuevo post en Fairbase en la direccion /user/nombre del usuario
                
            buff = '' #Se vacia variable
            
            
            
except KeyboardInterrupt: #Metodo de intorrupcion por teclado
   sys.stdout.flush()
   pass