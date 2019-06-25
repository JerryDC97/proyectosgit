import random

#Programa vecindades

# Crea la matriz de 0's
def crear_matriz(matriz, tamanio):
    for i in range(tamanio):
        matriz.append([])
        for j in range(tamanio):
            matriz[i].append(0)
    return


# Coloca las celulas en la print_matriz
def llenar_matriz(matriz, celulas):
    contador = 0
    while contador < celulas:
        i = random.randint(0,len(matriz[0])-1)
        j = random.randint(0,len(matriz[0])-1)
        if matriz[j][i] == 0:
            matriz[j][i] = 1
            contador += 1
        i=0
        j=0
    return


# Imprime la matriz
def print_matriz(matriz):
    for i in range(len(matriz[0])):
        print(matriz[i])
    print()
    return


# Obtiene la cantidad de vecinos en vecindad 4
def vecindad4(matriz, x, y):
    # Esquina superior izquierda
    if x == 0 and y == 0:
        cont = 0
        cont += matriz[1][0]
        cont += matriz[0][1]
        cont += matriz[len(matriz[0])-1][0]
        cont += matriz[0][len(matriz[0])-1]
    # Esquina superior derecha
    elif x == len(matriz[0])-1 and y == 0:
        cont = 0
        cont += matriz[0][x-1]
        cont += matriz[1][x]
        cont += matriz[0][0]
        cont += matriz[x][x]
    # Esquina inferior izquierda
    elif x == 0 and y == len(matriz[0])-1:
        cont = 0
        cont += matriz[y][x+1]
        cont += matriz[y-1][x]
        cont += matriz[y][y]
        cont += matriz[x][x]
    # Esquina inferior derecha
    elif x == len(matriz[0])-1 and y == len(matriz[0])-1:
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y][x-1]
        cont += matriz[y][0]
        cont += matriz[0][x]
    # Primera fila
    elif (x > 0 and x < len(matriz[0])-1) and y == 0:
        cont = 0
        cont += matriz[y][x-1]
        cont += matriz[y][x+1]
        cont += matriz[y+1][x]
        cont += matriz[len(matriz[0])-1][x]
    # Ultima fila
    elif (x > 0 and x < len(matriz[0])-1) and y == len(matriz[0])-1:
        cont = 0
        cont += matriz[y][x-1]
        cont += matriz[y][x+1]
        cont += matriz[y-1][x]
        cont += matriz[0][x]
    # Primera columna
    elif x == 0 and (y > 0 and y < len(matriz[0])-1):
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y+1][x]
        cont += matriz[y][x+1]
        cont += matriz[y][len(matriz[0])-1]
    # Ultima columna
    elif x == len(matriz[0])-1 and (y > 0 and y < len(matriz[0])-1):
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y+1][x]
        cont += matriz[y][x-1]
        cont += matriz[y][0]
    # El resto de la matriz
    else:
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y+1][x]
        cont += matriz[y][x-1]
        cont += matriz[y][x+1]
    return cont


# Obtiene la cantidad de vecinos en vecindad 8
def vecindad8(matriz, x, y):
    # Esquina superior izquierda
    if x == 0 and y == 0:
        cont = 0
        cont += matriz[1][0]
        cont += matriz[0][1]
        cont += matriz[1][1]
        cont += matriz[len(matriz[0])-1][0]
        cont += matriz[len(matriz[0])-1][1]
        cont += matriz[len(matriz[0])-1][len(matriz[0])-1]
        cont += matriz[0][len(matriz[0])-1]
        cont += matriz[1][len(matriz[0])-1]
    # Esquina superior derecha
    elif x == len(matriz[0])-1 and y == 0:
        cont = 0
        cont += matriz[y][x-1]
        cont += matriz[y+1][x-1]
        cont += matriz[y+1][x]
        cont += matriz[y+1][0]
        cont += matriz[y][0]
        cont += matriz[x][0]
        cont += matriz[x][x]
        cont += matriz[x][x-1]
    # Esquina inferior izquierda
    elif x == 0 and y == len(matriz[0])-1:
        cont = 0
        cont += matriz[y][x+1]
        cont += matriz[y-1][x+1]
        cont += matriz[y-1][x]
        cont += matriz[y-1][y]
        cont += matriz[y][y]
        cont += matriz[x][y]
        cont += matriz[x][x]
        cont += matriz[x][x+1]
    # Esquina inferior derecha
    elif x == len(matriz[0])-1 and y == len(matriz[0])-1:
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y-1][x-1]
        cont += matriz[y][x-1]
        cont += matriz[0][x-1]
        cont += matriz[0][x]
        cont += matriz[0][0]
        cont += matriz[y][0]
        cont += matriz[y-1][0]
    # Primera fila
    elif (x > 0 and x < len(matriz[0])-1) and y == 0:
        cont = 0
        cont += matriz[y][x-1]
        cont += matriz[y][x+1]
        cont += matriz[y+1][x]
        cont += matriz[y+1][x-1]
        cont += matriz[y+1][x+1]
        cont += matriz[len(matriz[0])-1][x]
        cont += matriz[len(matriz[0])-1][x-1]
        cont += matriz[len(matriz[0])-1][x+1]
    # Ultima fila
    elif (x > 0 and x < len(matriz[0])-1) and y == len(matriz[0])-1:
        cont = 0
        cont += matriz[y][x-1]
        cont += matriz[y][x+1]
        cont += matriz[y-1][x]
        cont += matriz[y-1][x-1]
        cont += matriz[y-1][x+1]
        cont += matriz[0][x]
        cont += matriz[0][x-1]
        cont += matriz[0][x+1]
    # Primera columna
    elif x == 0 and (y > 0 and y < len(matriz[0])-1):
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y+1][x]
        cont += matriz[y][x+1]
        cont += matriz[y-1][x+1]
        cont += matriz[y+1][x+1]
        cont += matriz[y][len(matriz[0])-1]
        cont += matriz[y-1][len(matriz[0])-1]
        cont += matriz[y+1][len(matriz[0])-1]
    # Ultima columna
    elif x == len(matriz[0])-1 and (y > 0 and y < len(matriz[0])-1):
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y+1][x]
        cont += matriz[y][x-1]
        cont += matriz[y-1][x-1]
        cont += matriz[y+1][x-1]
        cont += matriz[y][0]
        cont += matriz[y-1][0]
        cont += matriz[y+1][0]
    # El resto de la matriz
    else:
        cont = 0
        cont += matriz[y-1][x]
        cont += matriz[y+1][x]
        cont += matriz[y][x-1]
        cont += matriz[y-1][x-1]
        cont += matriz[y+1][x-1]
        cont += matriz[y][x+1]
        cont += matriz[y-1][x+1]
        cont += matriz[y+1][x+1]
    return cont


# Codigo principal
matriz = []
crear_matriz(matriz, 100)
llenar_matriz(matriz, 500)
print("-------MATRIZ DE CELULAS-------")
print_matriz(matriz)
print("----------VECINDAD 4----------")
# i son x y j son y
for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
        if matriz[j][i] == 1:
            print("CELULA({},{}) tiene una vecindad de {}".format(i, j, vecindad4(matriz,i,j)))
print("----------VECINDAD 8----------")
# i son x y j son y
for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
        if matriz[j][i] == 1:
            print("CELULA({},{}) tiene una vecindad de {}".format(i, j, vecindad8(matriz,i,j)))
