#Creo mi Tupla
mi_tupla = (1, "dos", 3.5, (4,5), True)

#Imprimo para saber cual es su longitug
print(len(mi_tupla))

#Imprimo que tipo de objeto
print(type(mi_tupla))

#Cambio la Tupla a Lista
mi_tupla = list(mi_tupla)

#Confirmo el cambio de objeto
print(type(mi_tupla))

#Creo un diccionario
dic = {'c1': mi_tupla[0], 'c2': mi_tupla[1], 'c3': mi_tupla[2],'c4': mi_tupla[3],'c5': mi_tupla[4]}

#Imprimo el diccionario
print(dic)
print(dic['c4'][0])