import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# retorna un csv
def getCSV(filePath):
    df = pd.read_csv(filePath)
    return df

# imprime el nombre de las columnas
def colnames(df):
    for col in df.columns:
        columns = []  
        columns.append(str(col))
    print(columns)

# retorna solo los elementos unicos de un arreglo
def unique(array):
    unique_list = []
    for x in array:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# retorna solo los tokens limpios (quita espacios a la izquierda o derecha) de una columna
def colvals(df, colname):
    collist = []
    clean_collist = []
    collist = df[colname].tolist()
    for token in collist:
        token = token.strip()
        clean_collist.append(token)
    return clean_collist

# retorna un diccionario con los elementos de una columna y el conteo de apariciones de los mismos 
def countInstances(colvals):
    results = {}
    unique_elems = unique(colvals)
    instances = []
    counter = 0
    for unique_elem in unique_elems: # recorre el arreglo de unicos
        for instance_of_elem in colvals: # contador de instancias elementos unicos
            if str(unique_elem) == str(instance_of_elem):
                counter += 1
        instances.append(counter)
        counter = 0
    results['elements'] = unique_elems
    results['instances'] = instances
    return results

# plotea 2 columnas, una de tokens y otra de valores o instancias, se evalua con <= threshold
def quickPlot(xcol, ycol, threshold):
    if threshold != None:
        # construir un diccionario con las dos columnas (tokens e instancias). ej:
        # arr = { 'token':instancias,
        #     'token1':1,
        #     'token2':8 }
        arr_assoc = {}
        ignored_arr_assoc = {}
        pointer = 0
        for token in xcol:
            arr_assoc[token] = ycol[pointer]
            pointer += 1
        pointer = 0

        # filtrado de values con el threshold
        for key, value in list(arr_assoc.items()):
            # condicion de evaluacion de los valores de la columna
            if value <= threshold:
                ignored_arr_assoc[key] = value
                del arr_assoc[key]

        # impresion de los elementos ignorados por el anterior filtro
        print(ignored_arr_assoc)

        # generacion de la grafica
        sorted_arr_assoc = {key: value for key, value in sorted(arr_assoc.items(), key=lambda item: item[1])}
        plt.bar(sorted_arr_assoc.keys(), sorted_arr_assoc.values())
        plt.xlabel('Palabras')
        plt.ylabel('Instancias')
        plt.title('Frecuencia')
        plt.show()
    else:
        plt.bar(xcol, ycol)
        plt.xlabel('Palabras')
        plt.ylabel('Instancias')
        plt.title('Frecuencia')
        plt.show()


# ['np',
    #  'apellido paterno',
    #  'apellido materno',
    #  'nombre(s)',
    #  'escuela',
    #  'turno',
    #  'grado escolar',
    #  'grupo',
    #  'edad',
    #  'sexo',
    #  'version',
    #  'el_________ es una pelota de fuego',
    #  'a1',
    #  '__________ es una pelota de plata',
    #  'a2',
    #  'mi __________ es una pelota de pelos',
    #  'a3',
    #  'la frase pelota que canta tiene sentido?',
    #  'por que?',
    #  'a4s',
    #  'a4n',
    #  'explica lo que quiere decir mi hermanito es una pelota de gritos',
    #  'a5',
    #  'que otra cosa podria ser una pelota de pelos?',
    #  'por que?.1',
    #  'a6',
    #  'explica tu respuesta en la frase pelota de plata',
    #  'a7']

# Reemplazar la ruta de abajo para obtener el CSV
df = getCSV("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Secundaria/Prueba 1/1_h_sec_todo_de_prueba1.csv")
# Reemplazar el nombre de la columna que se quiere evaluar
a1 = colvals(df, 'el_________ es una pelota de fuego')
res = countInstances(a1)
# Generacion de la grafica, el ultimo numero indica el valor que se evaluara para determinar los elementos que se graficaran
# ej. Si es 3, todos los elementos cuyas instancias sean de 3 o menos no se graficaran pero se imprimiran en consola
quickPlot(res['elements'],res['instances'], 3)
