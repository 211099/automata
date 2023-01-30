trancisiones = [#ES,EL,ES
                [1,["0"],2],
                [1,["1"],18],
                [1,["2"],38],
                [1,["3"],45],
                [2,["1","2","3","4","5","6","7","8","9"],3],
                [3,["-"],4],
                [3,["/"],11],
                [4,["2"],5],
                [4,["3"],7],
                [4,["0"],9],
                [5,["0","1","2","3","4","5","6","7","8","9"],6],
                [6,["-"],52],
                [7,["0","1"],8],
                [8,["-"],52],
                [9,["1","2","3","4","5","6","7","8","9"],10],
                [10,["-"],52],
                [11,["2"],12],
                [11,["3"],14],
                [11,["0"],16],
                [12,["0","1","2","3","4","5","6","7","8","9"],13],
                [13,["/"],52],
                [14,["0","1"],15],
                [15,["/"],52],
                [16,["1","2","3","4","5","6","7","8","9"],17],
                [17,["/"],52],
                [18,["1","2"],19],
                [18,["3","4","5","6","7","8","9"],39],
                [19,["-"],20],
                [19,["/"],29],
                [20,["2"],21],
                [20,["3"],23],
                [20,["0"],25],
                [20,["1"],27],
                [21,["0","1","2","3","4","5","6","7","8","9"],22],
                [22,["-"],52],
                [23,["0","1"],24],
                [24,["-"],52],
                [25,["1","2","3","4","5","6","7","8","9"],26],
                [26,["-"],52],
                [27,["0","1","2"],28],
                [27,["3","4","5","6","7","8","9"],22],
                [28,["-"],52],
                [29,["0"],30],
                [29,["1"],32],
                [29,["2"],34],
                [29,["3"],36],
                [30,["1","2","3","4","5","6","7","8","9"],31],
                [31,["/"],52],
                [32,["0","1","2"],33],
                [32,["3","4","5","6","7","8","9"],35],
                [33,["/"],52],
                [34,["0","1","2","3","4","5","6","7","8","9"],35],
                [35,["/"],52],
                [36,["0","1"],37],
                [37,["/"],52],
                [38,["0","1","2","3","4","5","6","7","8","9"],39],
                [39,["-"],40],
                [39,["/"],47],
                [40,["0"],41],
                [41,["1"],43],
                [41,["1","2","3","4","5","6","7","8","9"],42],
                [42,["-"],52],
                [43,["0","1","2"],44],
                [44,["-"],52],
                [45,["0","1"],46],
                [46,["-"],40],
                [46,["/"],47],
                [47,["0"],48],
                [47,["1"],50],
                [48,["1","2","3","4","5","6","7","8","9"],49],
                [49,["/"],52],
                [50,["0","1","2"],51],
                [51,["/"],52],
                [52,["1","2","3","4","5","6","7","8","9"],53],
                [52,["0"],57],
                [53,["0","1","2","3","4","5","6","7","8","9"],54],
                [54,["0","1","2","3","4","5","6","7","8","9"],55],
                [55,["0","1","2","3","4","5","6","7","8","9"],56],
                [57,["1","2","3","4","5","6","7","8","9"],58],
                ] 



fecha = "21-02-01"
alfabeto = ["0","1","2","3","4","5","6","7","8","9","-","/"]
estados_finales = [54,58,56,58]


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
            for i in range(79):
                if elemento in alfabeto:
                    if estado_actual == trancisiones[i][0]:
                        if elemento in trancisiones[i][1]:
                            estado_actual = trancisiones[i][2]
                            print("estado actual: ", estado_actual)
                            auxiliar_str = auxiliar_str +  elemento
                            break
                else:
                    print("no se encuentra en el alfabeto")
                    break
        else:
            print("cadena no valida ")
            guardar_o_no_guardar = False

    if guardar_o_no_guardar == True and estado_actual in estados_finales:
        print("si")
        cadenas_recopiladas.append(auxiliar_str)
       
                    
                       
#la funcion valida si existe alguna trancision que salga del estado actual
def validar_estado_trancision():
     for i in  range(79):
        if estado_actual == trancisiones[i][0]:
            print ("estado actual: ", estado_actual, "transicion: ", trancisiones[i][0] )
            return True
            break


# def txt_palabras():
#     global datos2
#     datos2 = []
# with open('holamundo.txt', 'r', encoding="utf-8") as file:
#     for line in file:
#         datos2.extend(line.split(" "))
       


# def prueba():
#     if validar_estado_trancision() == False and validar_si_Es_estado_final() ==  


    

               
           
    
    
            

   

leer_trancisiones()
print(cadenas_recopiladas)

