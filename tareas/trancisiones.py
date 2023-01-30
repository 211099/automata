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


#la funcion lee cual es el camino que tomo para llegar al resultado 
def leer_trancisiones():
    global estado_actual
    global auxiliar_str
    global cadenas_recopiladas
    cadenas_recopiladas = []
    guardar_o_no_guardar = True 
    auxiliar_str = ""
    estado_actual = 1
    print("estado actual: ", estado_actual)

    for elemento in fecha:
        if validar_estado_trancision():
            for i in range(6):
                if estado_actual == trancisiones[i][0]:
                    if elemento in trancisiones[i][1]:
                        estado_actual = trancisiones[i][2]
                        print("estado actual: ", estado_actual)
                        auxiliar_str = auxiliar_str +  elemento
                        i = 6

        else:
            print("cadena no valida ")
            guardar_o_no_guardar = False

    if guardar_o_no_guardar == True:
        print("si")
        cadenas_recopiladas.append(auxiliar_str)
       
                    
                       
#la funcion valida si existe alguna trancision que salga del estado actual
def validar_estado_trancision():
     for i in  range(6):
        if estado_actual == trancisiones[i][0]:
            return True


# def prueba():
#     if validar_estado_trancision() == False and validar_si_Es_estado_final() ==  


    

               
           
    
    
            

   

leer_trancisiones()
print(cadenas_recopiladas)

