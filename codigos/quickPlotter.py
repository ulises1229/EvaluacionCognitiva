import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

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

# genera un CSV con la lista pasada como param y lo guarda en el directorio raiz, NO lo retorna
# la lista como param tendra el nombre de las columnas
def generateCSV(colnames_list, base_dict, filename):
    pass
    # try:
    #     new_filename = filename + ".txt"
    #     with open(new_filename, 'w+') as textfile:
    #         array = list(base_dict.items())
    #         for x in array:
    #             for y in x:
    #                 textfile.write(x[0]+": "+str(y[0][0]))
    # except IOError:
    #     print("I/O error")
    # try:
    #     new_filename = filename + ".csv"
    #     with open(new_filename, 'w+') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=colnames_list)
    #         writer.writeheader()
    #         for key, value in list(base_dict.items()):
    #             writer.writerow({key:value})
    # except:
    #     pass
    # try:
    #     new_filename = filename + '.csv'
    #     with open(new_filename, 'w+') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=colnames_list)
    #         writer.writeheader()
    #         for data in base_dict:
    #             print(str(data))
    #             writer.writerow(str(data))
    # except IOError:
    #     print("I/O error")

# plotea 2 columnas, una de tokens y otra de valores o instancias, se evalua con <= threshold
# PARAMS
# xcol - list
# ycol - list
# threshold - valor que evaluara el numero minimo de instancias
# genCSV - True o False, permite la generacion o no de un CSV de los elementos ignorados por el threshold
def quickPlot(xcol, ycol, threshold, genCSV):
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
        # impresion de los elementos ignorados por el anterior filtro
        # if genCSV == True:
        #     generateCSV(['Palabra','Instancias'],ignored_arr_assoc,'El _ es una pelota de fuego')

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

# Reemplazar la ruta de abajo para obtener el CSV
df = getCSV("C:/Users/Drablaguna/Desktop/UNAM/SECUNDARIA_TODO.csv")
# Reemplazar el nombre de la columna que se quiere evaluar
a1 = colvals(df, 'el_es_una_pelota_de_fuego')
res = countInstances(a1)
# Generacion de la grafica, el ultimo numero indica el valor que se evaluara para determinar los elementos que se graficaran
# ej. Si es 3, todos los elementos cuyas instancias sean de 3 o menos no se graficaran pero se imprimiran en consola
quickPlot(res['elements'],res['instances'], 3, True)
# quickPlot(res['elements'],res['instances'], None)