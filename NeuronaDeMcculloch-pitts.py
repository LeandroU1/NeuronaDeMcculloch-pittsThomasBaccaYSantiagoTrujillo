def neuronas(entrada, peso, umbral):
    suma = 0
    for i in range(len(entrada)):
        suma += entrada[i] * peso[i]
    if suma >= umbral:
        return 1
    else:
        return 0

def funcion_and():
    lista=[[0,0],[0,1],[1,0],[1,1]]
    peso = [1,1]
    umbral = 2
    print ("AND")
    for i in lista:
        salida = neuronas(i,peso,umbral)
        print(salida)

def funcion_or():
    lista=[[0,0],[0,1],[1,0],[1,1]]
    peso = [1,1]
    umbral = 1
    print ("or")
    for i in lista:
        salida = neuronas(i,peso,umbral)
        print(salida)

def funcion_nor():
    lista=[[0,0],[0,1],[1,0],[1,1]]
    peso = [-1,-1]
    umbral = -1
    print ("nor")
    for i in lista:
        salida = neuronas(i,peso,umbral)
        print(salida)

def funcion_nand():
    lista=[[0,0],[0,1],[1,0],[1,1]]
    peso = [-1,-1]
    umbral = -2
    print ("nand")
    for i in lista:
        salida = neuronas(i,peso,umbral)
        print(salida)

def funcion_not():
    lista=[[0],[1]]
    peso = [-1]
    umbral = 0
    print ("not")
    for i in lista:
        salida = neuronas(i,peso,umbral)
        print(salida)

funcion_and()
print()
funcion_or()
print()
funcion_nor()
print()
funcion_nand()
print()
funcion_not()

#Punto 2

def neuronas(entrada, peso, umbral):
    suma = 0
    for i in range(len(entrada)):
        suma += entrada[i] * peso[i]
    if suma >= umbral:
        return 1
    else:
        return 0
    
def funcion_and2(a,b):
    return neuronas([a,b], [1,1], 2)

def funcion_or2(a,b):
    return neuronas([a,b], [1,1], 1)

def funcion_not2(a):
    return neuronas([a], [-1], 0)

def funcion_xor():
    lista=[[0,0],[0,1],[1,0],[1,1]]
    print("XOR")
    for par in lista:
        parte1 = funcion_and2(par[0], funcion_not2(par[1]))
        parte2 = funcion_and2(funcion_not2(par[0]), par[1])
        salida = funcion_or2(parte1, parte2)
        print(par, salida)

funcion_xor()

def funcion_xorn():
    lista=[[0,0],[0,1],[1,0],[1,1]]
    print("XOR")
    for par in lista:
        parte1 = funcion_and2(par[0], funcion_not2(par[1]))
        parte2 = funcion_and2(funcion_not2(par[0]), par[1])
        salida = funcion_or2(parte1, parte2)
        print(par, funcion_not2(salida))

funcion_xorn()