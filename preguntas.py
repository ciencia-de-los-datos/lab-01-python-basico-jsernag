"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """

    
    # suma = 0

    # with open("data.csv") as archivo_csv:
    #     file = csv.reader(archivo_csv)
        

    #     for line in file:
    #         lista = list(line)
    #         lista2 = list(lista[0])
    #         num = int(lista2[2])
    #         suma += num

    # print(lista)
    # print(lista2)




    # return suma
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)

    sumandos = [int(lista2[1]) for lista2 in lista[0:]]

    return sum(sumandos)




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    
    x = [y[0] for y in lista]
    unicos = set(x)
    listafinal = []
    for i in unicos:
        cant = x.count(i)
        tupla = (i, cant)
        listafinal.append(tupla)

    listafinalordenada = sorted(listafinal)
    return listafinalordenada



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)

    x = [y[0:2] for y in lista]
    
    a = []
    b =[]
    diccionario = {}

    for i,j in x:
        num = int(j)
        a.append((i,num))

    for key, value in a:

        if key not in diccionario.keys():
            diccionario[key] = 0

        diccionario[key] += value

    for key, value in diccionario.items():
        tupla = (key, value)
        b.append(tupla)

    listafinal = sorted(b)

    return listafinal





def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)

    x = [y[2].split("-") for y in lista]
    y = [z[1] for z in x]
    z = set(y)
    listafinal = []

    for i in z:
        cant = y.count(i)
        tupla = (i, cant)
        listafinal.append(tupla)

    listafinal = sorted(listafinal)


    return listafinal


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    
    letters = [(x[0], int(x[1])) for x in lista]
    listletter = set([x[0] for x in lista])
    result = []

    for i in listletter:
        temp = list(filter(lambda x: x[0] == i, letters))
    
        result.append((i, max(temp)[1], min(temp)[1]))
    

    result.sort()

    return result
    
                      


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    
    col5 = [x[4].split(",") for x in lista]
    unicos = []
    for i in col5:
        z = len(i)
        for j in range(z):
            v = i[j]
            unicos.append((v[:3],int(v[4:])))

    diccionario = {}

    for key,value in unicos:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    lista_final =[]

    for key in diccionario.keys():
        tupla = (key, min(diccionario[key]), max(diccionario[key]))
        lista_final.append(tupla)

    lista_final.sort()

    
      
    
    

    return lista_final
    



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    lista2 =[(x[0],x[1]) for x in lista]
    diccionario = {}
    for value,key in lista2:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    lista_final =[]

    for key,value in diccionario.items():
        tupla = (int(key), (value))
        lista_final.append(tupla)

    lista_final.sort()


    return lista_final

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    lista2 =[(x[0],x[1]) for x in lista]
    diccionario = {}
    for value,key in lista2:
        if key not in diccionario.keys():
            diccionario[key] = []
        diccionario[key].append(value)

    lista_final =[]

    for key,value in diccionario.items():
        tupla = (int(key), sorted(list(set(value))))
        lista_final.append(tupla)

    lista_final.sort()


    return lista_final
    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    
    col5 = [x[4].split(",") for x in lista]
    unicos = []
    for i in col5:
        z = len(i)
        for j in range(z):
            v = i[j]
            unicos.append(v[:3])

    unicos.sort()

    diccionario = {}

    for key in unicos:
        if key not in diccionario.keys():
            diccionario[key] = 0
        diccionario[key] += 1

    return diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    
    elementos = [(x[0],x[3].split(","),x[4].split(",")) for x in lista]
    lista_final = []
    for i in elementos:
        tupla = (i[0], len(i[1]), len(i[2]))
        lista_final.append(tupla)
    return lista_final



def pregunta_11():

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    lista2 = []
    elementos = [(x[3].split(","), int(x[1])) for x in lista]
    for i in range(len(elementos)):
        a = len(elementos[i][0])
        b = elementos[i][1]

        for j in range(a):
            c = elementos[i][0][j]
            lista2.append((c,b))

    diccionario ={}
    for key, value in sorted(lista2):
        if key not in diccionario.keys():
            diccionario[key] = 0
        diccionario[key] += value

    return diccionario


   



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    lista = []
    with open("data.csv","r") as archivo_csv:
        file = csv.reader(archivo_csv, delimiter="\t")
        for line in file:
            lista.append(line)
    lista2 = []
    elementos = [(x[0], x[4].split(",")) for x in lista]

    for i in elementos:
        long = len(i[1])
        for j in range(long):
            a = i[1][j]
            lista2.append((i[0], (int(a[4:]))))

    lista2.sort()
    diccionario ={}
    for key,value in lista2:
        if key not in diccionario.keys():
            diccionario[key] = 0
        diccionario[key] += value


    return diccionario

