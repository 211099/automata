trancisiones = [#ES,EL,ES
                # [1,["1"],2], #posicion de la trancision  = 0
                # [1,["0"],3],    #posicion de la trancision  = 1
                # [2,["0","1","2"],4],    #posicion de la trancision  = 2
                # [3,["1","2","3","4","5","6","7","8","9"],5] #posicion de la trancision  = 3
                [1,["0"],2],
                [1,["1","2"],3],
                [1,["3"],6],
                [2,["1","2","3","4","5","6","7","8","9"],4],
                [3,["0","1","2","3","4","5","6","7","8","9"],5],
                [6,["0","1"],7]
                ] 



fecha = "31"
estados_finales = [4,5,7]

# Ejemplo con un argumento

def leer_trancisiones():
    global estado_actual
    estado_actual = 1


    print("estado actual: ", estado_actual)
    
    if len(fecha) == 2:
        for elemento in fecha:
            for i in range(6):
                
                if estado_actual == trancisiones[i][0]:
                    if elemento in trancisiones[i][1]:
                        estado_actual = trancisiones[i][2]
                        print("estado actual: ", estado_actual)
                        i = 6
    

               
           
    
    
            

   
# for i in range(10, 33):
#     fecha_int = int(fecha)
#     auxiliar = fecha_int + 1
#     auxiliar_str = str(auxiliar)
#     fecha = auxiliar_str
#     print(fecha)
leer_trancisiones()
